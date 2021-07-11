# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

s = "()))(("
arr = []
count = 0
for i in s:
    if (i == "("):
        arr.append(i)
    else:
        if arr != []:
            arr.pop()
        else:
            count += 1
print(count + len(arr))