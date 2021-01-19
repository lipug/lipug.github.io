import multiprocessing as mp
from time import sleep


def simple_func():
    print('Starting simple func')
    sleep(1)
    print('Finishing simple func')


if __name__ == '__main__':
    p = mp.Process(target=simple_func)
    p.start()
    print('Waiting for simple func to end')
    p.join()