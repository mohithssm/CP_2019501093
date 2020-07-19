# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




def fun_nth_additive_prime(n):
	count = 1
	while n >= 0:
		if fun_is_prime(count) and addictive_number(count):
			count = count + 1
		else:
			break
	return count


def fun_is_prime(n):
	if n > 1:
		for i in range(2, n//2):
			if n%i == 0:
				return False
				break
		return True
	else:
		return False

def addictive_number(n):
	lst = []
	while n > 0:
		digit = n % 10
		n = n // 10
		lst.append(digit)
	total = sum(lst)
	if fun_is_prime(total):
		return True
	else:
		return False

print(fun_nth_additive_prime(5))