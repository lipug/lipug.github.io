import multiprocessing as mp
import time

def foo(q):
    time.sleep(20)
    q.put('hello')
    print('hello....')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()