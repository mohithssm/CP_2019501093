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
	x = 0
	lst = []
	while num > 0:
		rem = num % 10
		lst.append(rem)
		num = num // 10
	print(num % lst[-1])
	if num % lst[-1] == 0 and num % lst[-1]**2 == 0:
		return True
	else:
		return False  		

print(isPower(23))