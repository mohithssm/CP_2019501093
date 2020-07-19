# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2




def fun_nth_palindromic_prime(n):
	count = 1
	while n >= 0:
		if  is_palindrome(count):
			if  fun_is_prime(count):
				n = n - 1
		count = count + 1
	return count - 1

def fun_is_prime(n):
	if n > 1:
		for i in range(2, (n//2) + 1):
			if n%i == 0:
				return False
				break
		return True
	else:
		return False

def is_palindrome(n):
	temp = n
	rev = 0
	while n > 0:
		digit = n % 10
		rev = rev * 10 + digit
		n = n // 10
	if temp == rev:
		return True
	else:
		return False


print(fun_nth_palindromic_prime(10))


