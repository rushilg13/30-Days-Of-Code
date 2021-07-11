# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
# Tasks could be done in any order. Each task is done in one unit of time. 
# For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), 
# that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

tasks = ["A","A","A","B","B"]
dic = {}
n = 2
for i in tasks:
    dic[i] = tasks.count(i)
count_arr = list(dic.values())
count_arr.sort(reverse=True)
max_num = count_arr[0]
i = 0
counter = 0
while i < len(count_arr) and count_arr[i] == max_num:
    counter += 1
    i += 1
ret = (max_num - 1) * (n + 1) + counter
print(max(ret, len(tasks)))