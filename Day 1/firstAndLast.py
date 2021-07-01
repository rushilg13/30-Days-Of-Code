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

