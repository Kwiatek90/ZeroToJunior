import json 
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)

types = {'image/jpeg', 'image/png'}

def get_linkes(client_id):
    headers = {'Authorization': f'Client-ID {client_id}'}
    req = Request('https://api.imgur.com/3/gallery/random/random/', headers=headers, method='GET')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

    with urlopen(req) as resp: 
        data = json.loads(resp.read().decode('utf-8'))
    return [item['link'] for item in data['data'] if 'type' in item and item['type'] in types]

def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    with urlopen(link) as image, download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloades %s', link)
    
def setup_download_dir():
    download_dir = Path('Python\Wielowatkowosc_multithreading_multiproccesing/imgur/images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir
