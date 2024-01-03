from collections.abc import Callable, Iterable, Mapping
import logging
import os
from time import time
from queue import Queue
from threading import Thread
from typing import Any


from download import setup_download_dir, get_linkes, download_link

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DownloadWorker(Thread):
    
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        while True:
            directory, link = self.queue.get()
            try:
                download_link(directory, link)
            finally:
                self.queue.task_done()
                

def main():
    ts = time()
    client_id = os.getenv('d0d8af759e1cef6') 
    if  client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_linkes(client_id)
    
    queue = Queue()
    for x in range(8):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    
    for link in links:
        logger.info(f'Queueing {link}')
        queue.put((download_dir, link))
        
    queue.join()
        
    logging.info('Took %s seconds', time() - ts)
    
if __name__ == '__main__':
    main()