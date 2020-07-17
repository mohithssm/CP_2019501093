# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	n = len(a)
	s = sorted(a)
	i = (n-1)//2
	if n == 0:
		return None
	elif(n%2):
		return s[i]
	else:
		return (s[i]+s[i+1])/2.0
