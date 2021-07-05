# Given a linked list, Reverse it

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def append(self, data):
        newNode = Node(data)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp  = temp.next
            temp.next = newNode
    
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
    
    def reverse(self):
        if self.start == None:
            print("Empty!")
            return
        if self.start.next == None:
            print(self.start.value, "-> NULL")
        if self.start.next.next == None:
            print(self.start.next.value, "->" , self.start.value, "NULL")
        else:
            t1 = self.start
            t2 = self.start
            t3 = self.start.next
            while t3.next != None:
                if t1 == self.start:
                    t1.next = None
                    t2 = t3
                    t3 = t3.next
                    t2.next = t1
                    t1 = t2
                else:
                    t2 = t3
                    t3 = t3.next
                    t2.next = t1
                    t1 = t2
            t3.next = t2
            while t3 != None:
                print(t3.value, end = " -> ")
                t3 = t3.next
            print("NULL")


List1 = LinkedList()
l1 = [1,2,3,4,5,6]
for i in l1:
    List1.append(i)
List1.view()
List1.reverse()