# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	lst = []
	if n == 0:
		return False
	if n < 0:
		n = abs(n)
	else:
		lst = [elem for elem in str(n)]

	print(lst)
	# for i in range(len(lst)):
	# 	if lst[i] == lst[i+1]:
	# 		return True
	# 	return False
hasconsecutivedigits(5231123123123)