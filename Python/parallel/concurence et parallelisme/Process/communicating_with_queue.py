import multiprocessing
import random
import time

class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item) 
            print (f"Process Producer : item {item} appended to queue {self.name}")
            time.sleep(1)
            print (f"The size of queue is {self.queue.qsize()}")
       
class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            time.sleep(2)
            item = self.queue.get(block=True)
            print (f'Process Consumer : item {item} popped \
                     from by {self.name} \n')
            time.sleep(1)


if __name__ == '__main__':
        queue = multiprocessing.Queue()
        process_producer = producer(queue)
        process_consumer = consumer(queue)
        process_producer.start()
        process_consumer.start()
        process_producer.join()
        time.sleep(10)
        process_consumer.terminate()
        process_consumer.join()

        
        
         
