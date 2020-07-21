# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
	lst = []
	for i in range(len(l)):
		for j in range(len(l[i])):
			lst.append(l[i][j])
	for elem in lst:
		if fun_is_prime(elem) == False:
			return True
		else:
			return False		



def fun_is_prime(n):
	if n > 1:
		for i in range(2, n//2):
			if n%i == 0:
				return False
		return True
	else:
		return False
