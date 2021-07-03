# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Approach - 1 - Hashmaps
arr = [1,2,3,4,1]
dic = {}
for i in arr:
    dic[i] = arr.count(i)
sum1 = 0
for i in dic.values():
    if i != 1:
        print(True)
        exit()
print(False)

# Approach - 2 - sort - O(nlog(n))
arr = [1, 2, 3, 4]
arr.sort()
for i in range(len(arr)-1):
    if (arr[i] == arr[i+1]):
        print(True)
        exit()
print(False)