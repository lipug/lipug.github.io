#Spawn (fork) a Process – Process Based Parallelism
import multiprocessing

def myFunc(i):
    print (f'calling myFunc from process n°: {i}')
    for j in range (0,i):
        print(f'output from myFunc is :{j}')
    return

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()

