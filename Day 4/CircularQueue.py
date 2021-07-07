# Design a Circular Queue

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.arr = [None for i in range(size)]
    
    def enQueue(self, value):
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = value

    def deQueue(self):
        self.front = (self.front + 1) % self.size
        self.arr[self.front] = None

    def get(self):
        print(self.arr[self.rear])
        pass

    def view(self):
        print(self.arr)

CQ = CircularQueue(5)
CQ.enQueue(1)
CQ.enQueue(2)
CQ.enQueue(3)
CQ.enQueue(4)
CQ.enQueue(5)
CQ.deQueue()
CQ.enQueue(99)
CQ.view()
CQ.get()