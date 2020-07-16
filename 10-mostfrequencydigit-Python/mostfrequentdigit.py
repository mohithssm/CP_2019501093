# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	count = 0
	n = [num for elem in str(n)]
	num1 = n[0]
	for elem in n:
		curr_freq = n.count(elem)
		if curr_freq > count:
			count = curr_freq
			num = elem
	return num1