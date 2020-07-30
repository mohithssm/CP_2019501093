def fun_nthtenlyprime(a):
	count = 0
	val = 2
	lst = []
	while count <= a:
		if fun_istenlyprime(val) and fun_istenlyprime(val):
			lst.append(val)
			count = count + 1
		val = val + 1
	print(lst)
	return val-1

def fun_istenlyprime(n):
    sum = 0
    while n != 0:
        rem = n % 10
        sum = sum + rem
        n = n / 10
    if sum == 10:
        return True
    else:
        return False

def fun_isprime(n):
	if n <= 1:
		return False
	elif n == 2 or n == 3:
		return True
	for i in range(2, n//2):
		if n%i == 0:
			return False
	return True

print(fun_nthtenlyprime(8))