# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	lst = []
	if n == 0:
		return False
	if n < 0:
		n = abs(n)
	while n > 0:
		num = n%10
		lst.append(num)
		n = n//10
	for i in range(len(lst)):
		if lst[i] == lst[i+1]:
			return True
		return False
	