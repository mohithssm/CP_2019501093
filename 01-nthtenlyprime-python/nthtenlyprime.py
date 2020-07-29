def fun_nthtenlyprime(a):
    pass


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