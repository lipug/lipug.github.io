import multiprocessing

class MyProcess(multiprocessing.Process):

    def run(self):
        print (f'called run method in {self.name}')
        return

if __name__ == '__main__':
    for i in range(10):
        process = MyProcess()
        process.start()
        process.join()

