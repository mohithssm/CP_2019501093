# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

def longestdigitrun(n):
	digit_lst = n_arr(n)
	size = 1
	max_size = 0
	dict_items = {}
	print(digit_lst)
	for i in range(len(digit_lst) - 1):
		if digit_lst[i] == digit_lst[i+1]:
			size = size + 1
	

		else:
			size = 1
	

			

		if digit_lst[i+1] not in dict_items.keys():
			dict_items[digit_lst[i+1]] = size
	return dict_items

def n_arr(n):
	digit_lst = []
	while n > 0:
		rem = n % 10
		digit_lst.append(rem)
		n = n // 10
	return digit_lst[::-1]


print(longestdigitrun(117773732))