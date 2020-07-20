# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




# def fun_nth_additive_prime(n):
# 	count = 1
# 	while n >= 0:
# 		if fun_is_prime(count) and addictive_number(count):
# 			n = n - 1	
# 		count = count + 1
# 	return count - 1


# def fun_is_prime(n):
# 	if n > 1:
# 		for i in range(2, (n//2)+1):
# 			if n%i == 0:
# 				return False
# 				break
# 		return True
# 	else:
# 		return False

# def addictive_number(n):
# 	# lst = []
# 	tot = 0
# 	while n > 0:
# 		digit = n % 10
# 		n = n // 10
# 		tot = tot + digit
# 		# lst.append(digit)
# 	# total = sum(lst)
	
# 	if fun_is_prime(tot):
# 		return True
# 	else:
# 		return False

def isprime(n):
		if n > 1:
			for i in range(2,(n//2) + 1):
				if n % i == 0:
					return False
			return True
		else:
			return False

def isadditive(n):
	su = 0
	while n > 0:
		rem = n % 10
		su += rem
		n = n // 10
	if isprime(su):
		return True
	else:
		return False

def fun_nth_additive_prime(n):
	var = 1
	while n >= 0:
		if isprime(var) and isadditive(var):
			n -= 1
		var += 1
	return var - 1

print(fun_nth_additive_prime(5))