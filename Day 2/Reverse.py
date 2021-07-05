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
        pass

List1 = LinkedList()
l1 = [1,2,3,4,5,6,7,8]
for i in l1:
    List1.append(i)
List1.view()
List1.reverse()