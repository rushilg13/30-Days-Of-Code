# Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 
# Person A will NOT friend request person B (B != A) if any of the following conditions are true:
# age[B] <= 0.5 * age[A] + 7
# age[B] > age[A]
# age[B] > 100 && age[A] < 100
# Otherwise, A will friend request B.
# Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.
# How many total friend requests are made?

# Approach - 2 - O(n^2)
arr = [20,30,100,110,120]
count = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        else:
            if arr[i] <= (0.5*arr[j]) + 7:
                count += 0
            elif arr[i] > arr[j]:
                count += 0
            elif (arr[i] > 100 and arr[j] < 100):
                count += 0
            else:
                count +=1
print(count)
