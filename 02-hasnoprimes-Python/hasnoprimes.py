# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
	lst = []
	for i in range(len(l)):
		for j in range(len(l[i])):
			lst.append(l[i][j])
	return lst

print(fun_hasnoprimes([[12,4,6],[8,12,14],[6,18]]))

