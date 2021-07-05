# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

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
    
    def add(self, List2):
        resList = LinkedList()
        carry = 0
        if ((self.start == None) or (List2.start == None)):
            print("LinkedList is Empty!")
            return
        temp1 = self.start
        temp2 = List2.start
        len1 = self.sizeOf()
        len2 = List2.sizeOf()
        if len1 > len2:
            while temp1 != None:
                a = temp1.value
                if temp2 == None:
                    b = 0
                else:
                    b = temp2.value
                var = a + b + carry
                if var <= 9:
                    carry = 0
                else:
                    carry = var // 10
                    var = var % 10
                resList.append(var)
                temp1 = temp1.next
                if temp2 != None:
                    temp2 = temp2.next
        else:
            while temp2 != None:
                b = temp2.value
                if temp1 == None:
                    a = 0
                else:
                    a = temp1.value
                var = a + b + carry
                if var <= 9:
                    carry = 0
                else:
                    carry = var // 10
                    var = var % 10
                resList.append(var)
                if temp1 != None:
                    temp1 = temp1.next
                temp2 = temp2.next
        if carry != 0:
            resList.append(carry)
        resList.view()

List1 = LinkedList()
List2 = LinkedList()
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l1.reverse()
l2.reverse()
for i in l1:
    List1.append(i)
for i in l2:
    List2.append(i)
List1.view()
List2.view()
List1.add(List2)