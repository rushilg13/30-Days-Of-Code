# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

num = "23"
dic = {
    "1" : [""],
    '2' : ["a", "b", "c"],
    '3' : ["d", "e", "f"],
    '4' : ['g', 'h', 'i'],
    '5' : ['j', 'k', 'l'],
    '6' : ['m', 'n', 'o'],
    '7' : ['p', 'q', 'r', 's'],
    '8' : ['t', 'u', 'v'],
    '9' : ['w', 'x', 'y', 'z']
    }
    
a1 = ['a', 'b']
b1 = ['a', 'b']
for i in a1:
    for j in b1:
        print(i+j)
