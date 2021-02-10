from datetime import datetime
import time
import os


print(datetime.now().time(), os.getpid(), os.getppid())


def f(nom):
    print("Dans f")

import multiprocessing
time.sleep(1)
p1 = multiprocessing.Process(target=f, args=['realprocess'])
p1.start()
p1.join()