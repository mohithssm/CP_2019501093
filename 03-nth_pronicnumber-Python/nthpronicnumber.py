# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
import math

def nthpronicnumber(n):
    count = 1
    while n>= 0:
        if isPronic(count):
            n = n - 1
        count = count + 1
    return count - 1

def isPronic(num):
	n = (int)(math.sqrt(num))
	if ((n)*(n+1) == num):
		return True
	else:
		return False

	