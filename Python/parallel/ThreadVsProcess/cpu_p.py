import time

N = 10000000

def fc(df):
  return sum(i for i in range(df[0], df[1]))

def elapse(f, *args):
    te0 = time.time()
    tcpu0= time.process_time()
    res = f(*args)
    return (f.__name__, args, time.process_time() - tcpu0, time.time()-te0, res)

print(elapse(fc, (0,N)))

decoupe = [(i*N+1, (i+1)*N) for i in range(4)]
print(decoupe)

def repartir_iter():
  return list(map (fc, decoupe))

print(elapse(repartir_iter))

import concurrent.futures
def repartir_thread():
  with concurrent.futures.ThreadPoolExecutor(4) as tp:
    return list(tp.map(fc, decoupe))

print(elapse(repartir_thread))

import multiprocessing
def repartir_process():
  with multiprocessing.Pool(4) as pp:
    return pp.map(fc, decoupe)

if __name__  == '__main__':
    print(elapse(repartir_process))