# Design a Linkedlist

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def AddAtHead(self, data):
        newNode = Node(data)
        if self.start == None:
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode

    def AddAtEnd(self, data):
        newNode = Node(data)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

    def sizeOf(self):
        size = 0
        if self.start == None:
            print("LinkedList is Empty!")
            return size
        else:
            temp = self.start
            size += 1
            while temp.next != None:
                size += 1
                temp = temp.next
            return size
    
    def AddAtIndex(self, data, index):
        if index < 0:
            print("Invalid Index")
            return
        if index >= self.sizeOf():
            print("Invalid Index")
            return
        if index == 0:
            self.AddAtHead(data)
        if index+1 == self.sizeOf():
            self.AddAtEnd(data)
        newNode = Node(data)
        count = index - 1
        temp = self.start
        while count != 0:
            temp = temp.next
            count -= 1
        newNode.next = temp.next
        temp.next = newNode

    def get(self, index):
        if index < 0:
            print("Invalid Index")
            return
        if index >= self.sizeOf():
            print("Invalid Index")
            return
        if index == 0:
            print(self.start.value)
        count = index
        temp = self.start
        while count != 0:
            temp = temp.next
            count -= 1
        print(temp.value)
    
    def DeleteAtIndex(self, index):
        if index < 0:
            print("Invalid Index")
            return
        if index >= self.sizeOf():
            print("Invalid Index")
            return
        if index == 0:
            self.start = self.start.next
        count = index - 1
        temp = self.start
        while count != 0:
            temp = temp.next
            count -= 1
        temp.next = temp.next.next

    def view(self):
        if self.start == None:
            print("LinkedList is Empty!")
            return
        else:
            temp = self.start
            while temp != None:
                print(temp.value, end=" -> ")
                temp = temp.next
            print("NULL")

List = LinkedList()
List.AddAtHead(3)
List.AddAtHead(2)
List.AddAtHead(1)
List.AddAtHead(0)
List.AddAtEnd(4)
List.AddAtIndex(99, 2)
List.get(4)
List.DeleteAtIndex(3)
List.view()