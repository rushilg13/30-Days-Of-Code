# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

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
                temp = temp.next
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
    
    def merge(self, List2):
        temp1 = self.start
        temp2 = List2.start
        holder = List2.start
        while holder != None:
            if temp2.value > temp1.value:
                holder = holder.next
                temp2.next = temp1.next
                temp1.next = temp2
                temp2 = holder
                temp1 = temp1.next.next
            else:
                holder = holder.next
                temp2.next = temp1
                temp1 = temp2
                temp2 = holder

List1 = LinkedList()
List1.append(1)
List1.append(3)
List1.append(5)
List1.view()
List2 = LinkedList()
List2.append(-1)
List2.append(0)
List2.view()
List1.merge(List2)
List2.view()