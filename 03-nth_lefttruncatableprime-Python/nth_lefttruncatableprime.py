# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def fun_nth_lefttruncatableprime(n):
    count = 1
    lst = []
    for i in range(5000):
        if is_left_truncatable_prime(i):
            lst.append(i)
    return lst[n]

def digit_count(num):
    count = 0
    while num > 0:
        num = num % 10
        count = count + 1
        num = num // 10
    return count

def is_left_truncatable_prime(n):
    if not fun_isprimeNum(n):
        return False
    else:
        digit = digit_count(n)
        for i in range(1, digit):
            num = n % (10**i)
            if fun_isprimeNum(num):
                return True
        return False

def fun_isprimeNum(n):
	if n > 1:
		for i in range(2, n):
			if n%i == 0:
				return False
		return True
	else:
		return False
