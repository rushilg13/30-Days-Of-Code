# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append(val)
            self.min.append(val)
        else:
            if self.stack[-1] < val:
                self.stack.append(val)
                self.min.append(self.min[-1])
            else:
                self.stack.append(val)
                self.min.append(val)
        
    def pop(self) -> None:
        if self.stack == []:
            print("Stack Empty")
            return ValueError
        else:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        if self.stack == []:
            print("Stack Empty")
            return ValueError
        else:
            print (self.stack[-1])

    def getMin(self) -> int:
        print (self.min[-1])

mini = MinStack()
mini.push(-2)
mini.push(0)
mini.push(-3)
mini.getMin()
mini.pop()
mini.top()
mini.getMin()