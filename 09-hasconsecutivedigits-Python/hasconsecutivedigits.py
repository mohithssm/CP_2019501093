# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	lst = []
	if n == 0 :
		return False
	if n < 0:
		n = abs(n)
	lst = [elem for elem in str(n)]
	if (len(lst) == 1):
			return False

	for i in range(len(lst)-1):
		if (lst[0] != lst[1]):
			return False
		if (lst[i]) == (lst[i+1]):
			return True
		else:
			pass

hasconsecutivedigits(-24)
