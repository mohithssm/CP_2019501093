# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

import itertools

def longestdigitrun(n):
	lst = n_arr(n)
	for key, group in itertools.groupby(lst):
		keyGroup = {key: len(list(group))}
		

		x = max(sum(1 for elem in l) for n, l in itertools.groupby(lst))
	print(keyGroup.get(key, x))
	return x

def n_arr(n):
	digit_lst = []
	while n > 0:
		rem = n % 10
		digit_lst.append(rem)
		n = n // 10
	return digit_lst[::-1]



print(longestdigitrun(117773732))