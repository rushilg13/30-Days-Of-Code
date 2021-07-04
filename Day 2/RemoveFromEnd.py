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
            print("NULL")
    
    def DeleteFromEnd (self, n, length):
        point1 = self.start
        count = length - n
        if length == n:
            self.start = None
            return ("LinkedList is Empty!")
        while count != 1:
            count -= 1
            point1 = point1.next
        point1.next = point1.next.next

myList=LinkedList()
arr = [1, 2, 3 ,4]
length = len(arr)
for i in arr:
    myList.append(i)
myList.view()
myList.DeleteFromEnd(4, length)
myList.view()