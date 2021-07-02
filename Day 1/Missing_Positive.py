# Given an unsorted integer array nums, find the smallest missing positive integer.

# Approach - 1 - O(n^2)
arr = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12]
i = 1
while(True):
    if i not in arr:
        print(i)
        break
    else:
        i += 1

# Approach - 2 - O(nlog(n)) + O(n) = O(nlog(n))
arr = [5, 4, 1, 2, 6]
arr.sort()
if arr[0] != 1:
    print(1)
else:
    for i in range(len(arr)-1):
        if(arr[i]+1 != arr[i+1]):
            print(arr[i]+1)

# Approach - 3 - Hashing - O(n) time and space
arr = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12]
dic = {}
for i in range(len(arr)):
    dic[arr[i]] = i
i = 1
while(True):
    if i not in dic:
        print(i)
        break
    else:
        i += 1

