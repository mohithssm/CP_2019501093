# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def nthcircularprime(n):
	i = 1
	count = 1
	while count <= n:
		if isprimeNum(i):
			c = 1
			x = i
			for j in range(len(str(i)) - 1):
				x = str(x)
				x = x[-1] + x[:len(x)-1]
				x = int(x)
				if isprimeNum(x) and x != i:
					c  = c + 1
			if c == len(str(i)):
				count = count + 1
		i = i + 1
	return i - 1

def isprimeNum(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n%2 == 0 and n%3==0:
		return False
	x = 5
	while x*x <= n:
		if (n%x == 0 or n%(x+2) == 0):
			return False
		x = x + 6
	return True
print(nthcircularprime(4))