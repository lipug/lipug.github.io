import os
import time
import threading
import multiprocessing
import random
from do_something import *
 
NUM_WORKERS = 10
size = 10000000
out_list = list()


#MultiThreading
'''
start_time = time.time()
jobs = []
for i in range(0, NUM_WORKERS):
    thread = threading.Thread(target=do_something(size, out_list))
    jobs.append(thread)
for j in jobs:
    j.start()
    
for j in jobs:
    j.join()

print ("List processing complete.")
end_time = time.time()
print("threading time=", end_time - start_time)
'''

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    procs = 10   
    jobs = []
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process\
                  (target=do_something,args=(size,out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print("multiprocesses time=", end_time - start_time)
