# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


def fun_nth_happy_number(n):
	count = 1
	while n >= 0:
		if ishappynumber(count):
			n = n - 1
		count = count + 1
	return count-1	
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