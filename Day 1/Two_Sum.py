# // Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# // You may assume that each input would have exactly one solution, and you may not use the same element twice.
# // You can return the answer in any order.

# Approach - 1 - O(n2)
arr = [2, 1, 5, 3]
target = 4
for i in range(0, len(arr)-1):
    for j in range(1, len(arr)):
        if(arr[i] + arr[j] == target):
            print([i, j])

# Approach - 2 - O(n)
arr = [1, 2, 3, 5]
target = 4
arr.sort()
front = 0
end = len(arr)-1
while(arr[front] + arr[end] != target):
    print(front, end)
    if(arr[front] + arr[end] > target):
        end -=1
    if(arr[front] + arr[end] < target):
        front +=1
print([front, end])

# Another Approach -3 (Using Hashmap)
arr = [2, 1, 5, 3]
target = 4
dic = {}
for i in range(len(arr)):
    dic[arr[i]] = i
for i in dic.keys():
    num = target - i
    if num in dic.keys() and (dic[i] != dic[num]):
        print(dic[i], dic[num])
        break

# Approach - 4 - (Using Hashmap) 
arr = [2, 1, 5, 3]
target = 4
hashMap = {}
for i in range(len(arr)):
    if((target - arr[i]) not in hashMap.keys()):
        hashMap[arr[i]] = i
    else:
        print([hashMap[target-arr[i]], i])


# Approach - 5 - (Using Hashmap)
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