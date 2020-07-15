# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	if (int(n)%2 == 0):
		temp1 = int(n) - 1
		temp2 = int(n) + 1
		if n - temp1 <= temp2 - n:
			return temp1
		elif n - temp1 > temp2 - n:
			return temp2
		else:
			return int(n) 


