# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def fun_nth_kaprekarnumber(n):
    i = 0
    count = -1
    while True:
        if fun_is_kaprekarnumber(i):
            count = count + 1
            if count == n:
                return i
        i = i + 1

def fun_is_kaprekarnumber(n):
    if n == 1:
        return True
    sq = n*n
    num = str(sq)
    lst = []
    for i in range(1, len(num)):
        x = int(num[0:i])
        y = int(num[i:])
        if x != 0 and y != 0:
            if x+y == n:
                return True
    return False
print(fun_is_kaprekarnumber(45))