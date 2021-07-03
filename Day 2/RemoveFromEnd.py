# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def append (self, data):
        newNode = Node(data)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

    def view (self):
        if self.start == None:
            print("LinkedList is Empty!")
        else:
            temp = self.start
            while temp != None:
                print(temp.value, end=" -> ")
                temp = temp.next
            print("End")
    
    def DeleteFromEnd (self, n):
        pass

myList=LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
arr = [9, 8, 7 ,6]
for i in arr:
    myList.append(i)
myList.view()