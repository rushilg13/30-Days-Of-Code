# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

# Approach - 1 (Use Brute Force)
# Generate all combinations and traverse through list to find the next permutation

# Approach -2 
arr = [3, 1, 2]
idx = -1
for i in range(len(arr)-1, 0, -1):
    if(arr[i] > arr[i-1]):
        idx = i
        break
print("idx:", idx)

if(idx==-1):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end='')

else:
    prev = idx
    for i in range(idx+1, len(arr)):
        if(arr[i]>arr[idx-1] and arr[i]<arr[prev]):
            prev = i
    arr[idx-1], arr[prev] = arr[prev], arr[idx-1]
    temp1 = (arr[:idx])
    temp2 = arr[idx:]
    temp2.reverse()
    print(temp1 + temp2)