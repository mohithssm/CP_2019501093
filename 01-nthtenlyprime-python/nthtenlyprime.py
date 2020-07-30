def fun_nthtenlyprime(a):
	count = 1
	while a >= 0:
		if fun_istenlyprime(count) and fun_istenlyprime(count):
			a = a - 1
		count = count + 1
	return count-1
		
def fun_istenlyprime(n):
    sum = 0
    while n != 0:
        rem = n % 10
        sum = sum + rem
        n = n // 10
    if sum == 10:
        return True
    else:
        return False

def fun_isprime(n):
	if n > 1:
		for i in range(2, n//2):
			if n%i == 0:
				return False
		return True
	else:
		return False


print(fun_nthtenlyprime(1))