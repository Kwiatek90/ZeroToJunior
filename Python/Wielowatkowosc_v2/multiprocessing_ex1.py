import time 
import multiprocessing

start = time.perf_counter()

def do_smth():
    print(f"Sleeping 1 second(s) ...")
    time.sleep(1)
    print("Done sleeping")
  
p1 = multiprocessing.Process(target=do_smth)
p2 = multiprocessing.Process(target=do_smth)

p1.start()
p2.start()

p1.join()
p2.join()
    
finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} second(s)")