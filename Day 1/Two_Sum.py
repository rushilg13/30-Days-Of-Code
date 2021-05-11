# // Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# // You may assume that each input would have exactly one solution, and you may not use the same element twice.
# // You can return the answer in any order.

# Approach - 1
arr = [2, 1, 5, 3]
target = 4
hashMap = {}
for i in range(len(arr)):
    if((target - arr[i]) not in hashMap.keys()):
        hashMap[arr[i]] = i
    else:
        print([hashMap[target-arr[i]], i])


# Approach - 2
nums = [2,1,5,3]
target = 4
dic = {}
for i in range(len(nums)):
    dic[nums[i]] = i
nums.sort()
i = 0
j = len(nums)-1
while(nums[i] != nums[j]):
    if(nums[i] + nums[j] > target):
        j = j-1
    elif(nums[i] + nums[j] < target):
        i = i+1
    else:
        i = dic[nums[i]]
        j = dic[nums[j]]
        print([i, j])                