# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def fun_nth_happy_number(n):
	count = 1
	while n>= 0:
		if ishappynumber(count) and isprimeNum(count):
			n = n - 1
		count = count + 1
	return count - 1

def ishappynumber(n):
	arr = []
	if n < 0:
		return False
	while n != 1:
		n = sum(int(i)**2 for i in str(n))
		if n in arr:
			return False
		arr.append(n)
	return True

def isprimeNum(n):
	if n > 1:
		for i in range(2, n//2):
			if n%i == 0:
				return False
				break
		return True
	else:
		return False

def fun_nth_happy_prime(n):
	return 0