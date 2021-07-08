# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

s = "3[a]2[c]"
arr = []
count = 0
string = ""
res = ""
for i in s:
    arr.append(i)
arr.reverse()
print(arr)
top = 0
while top != len(arr):
    if arr[top] == ']':
        top += 1
        count -= 1
    if arr[top] != "[":
        string = string + arr[top]
        top += 1
    if arr[top] == "[":
        top += 1
        count += 1
    if arr[top].isdigit() and count == 0:
        res += (int(arr[top])*string)
        string = ""
        top += 1
for i in range (len(res)-1, -1, -1):
    print(res[i], end='')