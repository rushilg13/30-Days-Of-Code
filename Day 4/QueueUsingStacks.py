# Implement a Queue using 2 Stacks

arr1 = []
arr2 = []
arr1.append(5)
arr1.append(4)
arr1.append(3)
arr1.append(2)
arr1.append(1)
arr1.append(0)
for i in range(len(arr1)):
    a = arr1.pop()
    arr2.append(a)
print(arr2)