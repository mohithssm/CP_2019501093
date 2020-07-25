# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	count = -1
	num = 308
	while True:
		if fun_isProperty309(num):
			count = count + 1
			if count == n:
				return num
		num = num + 1
	return

def fun_isProperty309(n):
	lst = list("0123456789")
	n = n**5
	num = str(n)
	for elem in lst:
		if elem not in num:
			return False
	return True