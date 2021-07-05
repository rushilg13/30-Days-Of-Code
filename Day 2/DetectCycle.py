# Given a linked list, check if the linked list has loop or not. Below diagram shows a linked list with a loop. 
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
    
    def detect(self):
        if self.start == None:
            print("LinkedList is Empty!")
            return False
        else:
            s = set()
            temp = self.start
            while temp != None:
                if temp.value in s:
                    print("Cycle Exists")
                    return True
                else:
                    s.add(temp.value)
                    temp = temp.next
            print("No cycle Exists")
            return False

List1 = LinkedList()
l1 = [1,2,3,4,5,6,7,8]
for i in l1:
    List1.append(i)
List1.view()
List1.detect()