import os

def fc(df):
  'Calcul la somme de tous les nombre de df[0] à df[1] (df[1] non compris)'
  print(f'---> {df} {os.getpid()} {os.getppid()}')
  return sum(i for i in range(df[0], df[1]))

from multiprocessing import Pool
import time

def fcallback(rep):
  print(f'Callback : {rep} {os.getpid()} {os.getppid()}')

def lance_aprocess(df, cb):
  '''Calcul dans une version thread
  la somme de tous les nombre de df[0] à df[1] (df[1] non compris)'''
  with Pool(1) as tp:
    rep = tp.apply_async(fc, [df], callback=cb)
    return rep.get()

if __name__  == '__main__':
  print(f'Je suis {os.getpid()} {os.getppid()}')
  rep = lance_aprocess((0,100000),fcallback)
  # vrep = rep.get()
  # print(vrep)
  '''
  with Pool(1) as tp:
    rep = tp.apply_async(fc, [(0,100000)], callback=fcallback)
    vrep = rep.get()
  '''
