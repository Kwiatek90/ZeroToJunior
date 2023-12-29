import time 
import concurrent.futures

start = time.perf_counter()

def do_smth(seconds):
    print(f"Sleeping {seconds} second(s) ...")
    time.sleep(seconds)
    return "Done sleeping"

if __name__ == '__main__':  
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        results = executor.map(do_smth, secs)
        
        for result in results:
            print(result)
            
    finish = time.perf_counter()

    print(f"Finished in {round(finish-start,2)} second(s)") 
  
#processes = [] 
  
#if __name__ == '__main__':  
#    for _ in range(10):
#        p = multiprocessing.Process(target=do_smth, args=[1.5])
#        p.start()
#        processes.append(p)
#        
#    for process in processes:
#         process.join()   
#        
