# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

s = "[]"
arr = []
if len(s) % 2 != 0:
    print(False)
    exit()
for i in s:
    if (i == "[") or (i == "{") or (i == "("):
        arr.append(i)
    elif (i == "]") or (i == "}") or (i == ")"):
        if arr[-1] == "[" and i == "]":
            arr.pop()
        elif arr[-1] == "{" and i == "}":
            arr.pop()
        elif arr[-1] == "(" and i == ")":
            arr.pop()
    if len(arr) == 0:
        print(True)
    else:
        print(False)