

# Approach - 1
arr = [2,3,4,5]
n = ""
for i in arr:
    n += str(i)
n = int(n)
print(n+1)

# Approach - 2
arr = [2,3,4,5]
n = 0
t = 1
for i in range(len(arr)-1, -1, -1):
    n += arr[i]*t
    t = t*10
print(n+1)

# Approach - 3
arr = [9,9,9]
if arr[-1] != 9:
    arr[-1] += 1
else:
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 9:
            arr[i] = 0
        else:
            arr[i] += 1
            break
if(min(arr) == max(arr) == 0):
    arr.append(0)
    arr[0] = 1
print(arr)