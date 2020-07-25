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
    while n>= 0:
        if not is_left_truncatable_prime(count):
            n = n - 1
        count = count + 1
    return count - 1


def is_left_truncatable_prime(n):
    if not fun_isprimeNum(n):
        return False
    num = str(n)

    for i in range(len(num)):
        if "0" in num[i:]:
            return False
        tr = int(num[i:])
        if not fun_isprimeNum(tr):
            return False
    return True


def fun_isprimeNum(n):
	if n > 1:
		for i in range(2, n//2):
			if n%i == 0:
				return False
				break
		return True
	else:
		return False


print(fun_nth_lefttruncatableprime(5))