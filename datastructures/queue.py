# Using Collections deque
from collections import deque

class QueueCollections:
    def __init__(self):
        self.queue = deque()

    def push(self, value):
        return self.queue.append(value)
    
    def pop(self):
        return self.queue.popleft()


# Using List
class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, value):
        return self.queue.append(value)

    def pop(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]
    
    def printQueue(self):
        print(self.queue)
    

my_queue = Queue()

my_queue.push(1)
my_queue.push(2)

my_queue.printQueue()
my_queue.pop()
my_queue.printQueue()
