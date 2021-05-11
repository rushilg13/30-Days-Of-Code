arr = [-1, 0, 1, 2, -1, -4]
arr.sort()
res = []
s = set()
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if(i!=j and j !=k and (arr[i] + arr[j] + arr[k]==0)):
                res.append([arr[i], arr[j], arr[k]])
