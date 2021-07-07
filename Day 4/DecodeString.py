# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

s = "3[a]2[bc]"
num = 0
front = -1
rear = -1
for i in s:
    if (i != "[") and (i != "]"):
        if (i.isdigit()):
            num = int(i)
        else:
            print(i*num, end='')