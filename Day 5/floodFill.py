# o perform a flood fill, consider the starting pixel, 
# plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
#  plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
# Replace the color of all of the aforementioned pixels with newColor.

class Queue:
    def __init__(self) -> None:
        self.arr = []
    
    def enQueue(self, val):
        self.arr.append(val)
    
    def deQueue(self):
        pop = self.arr[0]
        self.arr.remove(self.arr[0])
        return pop

    def isEmpty(self):
        if self.arr == []:
            return True
        else:
            return False

image =[[1,1,1],
        [1,1,0],
        [1,0,1]]
sr = 1
sc = 1
newColor = 2

