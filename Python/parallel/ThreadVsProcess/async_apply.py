import os

def fc(df):
  'Calcul la somme de tous les nombre de df[0] à df[1] (df[1] non compris)'
  print('---> {df} {os.getpid} {os.getppid}')
  return sum(i for i in range(df[0], df[1]))

from multiprocessing import Pool
import time


if __name__  == '__main__':
  with Pool(1) as tp:
    rep = tp.apply_async(fc, [(0,100000)])
    vrep = rep.get()
