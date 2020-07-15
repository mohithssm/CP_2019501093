# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math

def isperfectsquare(n):
	# your code goes here
	if (type(n) == str or n < 0):
		return False
	elif (type(n) == int):
		if type(n) == str:
			try:
				n = int(n)
			except:
				return False
		num = math.sqrt(n)
		if num**2 == n:
			return True
		return False
	else:
		return False

