# nthPronicnber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
import math

def nthpronicnumber(n):
	count, v = 0, 0
	while count < n:
		v = v + 1
		if isPronic(v):
			count = count + 1
	return v

def isPronic(n):
	num = (int)(math.sqrt(n))
	if ((num)*(num+1) == n):
		return True
	else:
		return False

	