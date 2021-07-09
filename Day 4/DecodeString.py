# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

s = "3[a2[c]]"
arr = []
string = ""
res = ""
count = 0
for i in s:
    arr.append(i)
arr.reverse()
print(arr)
for i in arr:
    if i == "]":
        count -= 1
        string = ""
    if i.isalpha():
        string = string + i
    if i == "[":
        count += 1
    if i.isdigit():
        string = string*int(i)
        if count == 0:
            res += string
for i in range(len(res)-1, -1, -1):
    print(res[i], end='')