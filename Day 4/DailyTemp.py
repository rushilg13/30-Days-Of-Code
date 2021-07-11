# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead. 

# Approach - 1
temperatures = [73,74,75,71,69,72,76,73]
print(temperatures)
arr = []
for i in range(len(temperatures)):
    count = 0
    flag = 0
    for j in range(i+1, len(temperatures)):
        if temperatures[i] < temperatures[j]:
            count += 1
            arr.append(count)
            flag = 1
            break
        else:
            count += 1
if flag == 0:
    arr.append(0)
arr.append(0)
print(arr)