# Given a sorted array with possibly duplicate elements, the task is to find indexes of 
# first and last occurrences of an element x in the given array. 

# Approach - 1 - O(n)
arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
target = 5
front = 0
end = len(arr)-1
while(arr[front] != arr[end]):
    if(arr[front] < target):
        front +=1
    if(arr[end] > target):
        end -=1
print(front, end)

# Approach - 2 - O(log(n)) - INCOMPLETE
arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
target = 5
low = 0
res = [-1, -1]
high = len(arr)
while(low <= high):
    mid = int((low+high)//2)
    if(arr[mid] < target):
        low = mid + 1
    elif(arr[mid] == target):
        high = mid
        res[0] = mid
        res[1] = mid
    else:
        high = mid
    if res[0] == -1:
        print(res)
        break