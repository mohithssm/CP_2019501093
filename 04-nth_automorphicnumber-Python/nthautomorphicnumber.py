# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

import math

def nthautomorphicnumbers(n):
    count = 1
    while n>= 0:
        if isAutomorphic(count):
            n = n - 1
        count = count + 1
    return count - 1

def isAutomorphic(num):
	x = num**2
	print(x)
	if str(num) in str(x):
		return True
	else:
		return False

print(isAutomorphic(89065))