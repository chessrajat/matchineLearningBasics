from itertools import permutations
from itertools import combinations
import math

arr = ['H','O',"R","S","E"]
a = ["A","B","C","D"]
print(len(list(combinations(a,2))))
print(len(list(permutations(a,2))))

# print(list(combinations(arr,3)))

# In how many ways can 10 balls be picked, from 7 red out of 10, and 3 blue out of 8?

# red = math.factorial(10)/(math.factorial(7)*math.factorial(3))
# 6c3 + 5c2 6!/3!*3! + 5!/2!*3!
result = (math.factorial(6)/(math.factorial(3)*math.factorial(3)))*(math.factorial(5)/(math.factorial(2)*math.factorial(3)))
# print(red)
# n!/r!(n-r)!
print(result)