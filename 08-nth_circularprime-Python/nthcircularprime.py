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
	if n > 1:
		for i in range(2, n//2):
			if n%i == 0:
				return False
				break
		return True
	else:
		return False

print(nthcircularprime(4))