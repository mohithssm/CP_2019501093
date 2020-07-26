# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def nthlychrelnumbers(n):
	count, v = 1, 196
	while count < n:
		v = v + 1
		if isLychrelNum(v):
			count = count + 1
	return v

def isLychrelNum(num):
	palind = str(num)[::-1]
	for i in range(30):
		num = num + int(palind)
		if num == int(palind):
			return False
	return True