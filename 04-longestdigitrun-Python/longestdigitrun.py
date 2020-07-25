# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).


def longestdigitrun(n):
	if n < 0:
		n = abs(n)
	n = str(n)
	x = 0 
	y = 0 
	i = 0 
	count = 0 
	num = 0
	while y < len(n):
		while y < len(n) and n[x] == n[y]:
			y = y + 1
		if y - x == count:
			num = min(num, num[x])
		elif y - x > count:
			num = n[x]
			count = y - x
		if y == len(n):
			break
		x = y
	return int(num)
