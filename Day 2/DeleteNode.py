# Delete a Node in LinkedList

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
    
    def delete(self, data):
        if self.start == None:
            print("LinkedList is Empty!")
            return
        elif self.start.value == data:
            self.start = self.start.next
        else:
            temp = self.start
            while temp.next.value != data:
                temp = temp.next
            print(temp.value)
            temp.next = temp.next.next

List1 = LinkedList()
List1.append(1)
List1.append(3)
List1.append(5)
List1.append(0)
List1.append(9)
List1.view()
List1.delete(1)
List1.view()
