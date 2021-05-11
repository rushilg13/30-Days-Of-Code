# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and 
# nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

arr = [-4, -1, -1, 0, 1, 2]
res = []
arr.sort()
print(arr)
for i in range(len(arr)-2):
    if i!=0 and arr[i]==arr[i-1]:
        continue
    target = 0 - arr[i]
    j = i+1
    k = len(arr)-1
    while(k>j):
        total = arr[j] + arr[k]
        if(total > target):
            k = k-1
        elif(total < target):
            j = j+1
        elif(total == target):
            res.append([arr[i], arr[j], arr[k]])
            while(k>j and arr[j]==arr[j+1]):
                j+=1
            while(k>j and arr[k]==arr[k-1]):
                k-=1
            j=j+1
            k=k-1
print(res)