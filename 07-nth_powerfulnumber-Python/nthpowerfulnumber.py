# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def nthpowerfulnumber(n):
	if n == 0:
		return 1
	else:
		count = 1
		while n>= 0:
			if isPower(count):
				n = n - 1
			count = count + 1
		return count - 1

def isPower(num):
	count = 0
	st = primeFactors(num)
	for elem in st:
		if num % elem**2 == 0:
			count = count + 1
	if count == len(st):
		return True
	else:
		return False
def primeFactors(num):
	lst = []
	factors = []
	i = 2

	while i*i <= num:
		if num%i:
			i = i + 1
		else:
			 num = num // i
			 lst.append(i)
	if num > 1:
		lst.append(num)
	for elem in lst:
		if elem not in factors:
			factors.append(elem)
	return factors
		
