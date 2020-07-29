def fun_nthtenlyprime(a):
	count = 1
	while n >= 0:
		if fun_istenlyprime(count):
			n = n - 1
		count = count + 1
	return count-1
		
def fun_istenlyprime(n):
    pass


def fun_isprime(n):
	if n > 1:
		for i in range(2, n//2):
			if n%i == 0:
				return False
		return True
	else:
		return False