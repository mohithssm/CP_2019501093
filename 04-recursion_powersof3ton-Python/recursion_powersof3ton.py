# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

# def recursion_powersof3ton(n):
	
import math

def recursion_powersof3ton(n):
	if n < 1:
		return None
	num = power(n)
	if m < 3:
		return [1]
	else:
		return recursion_powersof3ton(3**num-1) +[3**num]
def power(n):
	if n < 3:
		return 0
	else:
		return 1 + power(math.floor(n)/3)
