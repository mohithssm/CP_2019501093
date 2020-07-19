# Write the function fun_isfactorish(n) that takes a value int n, 
# and returns True if n is a (possibly-negative) integer with exactly 3 unique digits 
# (so no two digits are the same), where each of the digits is a factor of the number 
# n itself. In all other cases, the function returns False (without crashing).
# For example:
#  assert(fun_isfactorish(412) == True) # 4, 1, and 2 are all factors of 412
#  assert(fun_isfactorish(-412) == True) # Must work for negative numbers!
#  assert(fun_isfactorish(4128) == False) # 4128 has more than 3 digits
#  assert(fun_isfactorish(112) == False) # 112 has duplicate digits (two 1's)
#  assert(fun_isfactorish(420) == False) # 420 has a 0 (0 is not a factor)
#  assert(fun_isfactorish(42) == False) # 42 has a leading 0 (only 2 unique digits)


def fun_isfactorish(n):
	num_lst = []
	if n < 0:
		n = abs(n)
	while n > 0:
		digit = n % 10
		n = n // 10
		num_lst.append(digit)
	num_lst = num_lst[::-1]
	if  n % num_lst[0] == 0 and  n % num_lst[1] == 0 and n % num_lst[2] == 0:
		return True
	else:
		return False 


print(fun_isfactorish(-412))

