# Given an unsorted integer array nums, find the smallest missing positive integer.

# Approach - 1 - O(n)
arr = [7,8,9,11,12]
sum1 = 0
sum2 = 0
mini = min(arr)
maxi = max(arr)
for i in range(mini, maxi +1):
    sum1 += i
for i in arr:
    sum2 += i
print(sum1-sum2)


# Approach - 2 - O(nlog(n))
arr = [5, 4, 1, 2, 6]
arr.sort()
for i in range(len(arr)-1):
    if (arr[i] + 1 != arr[i+1]):
        print(arr[i]+1)