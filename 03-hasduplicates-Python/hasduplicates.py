# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	lst = []
	count = 0
	for i in range(len(L)):
		for j in range(len(L[i])):
			if L[i][j] not in lst:
				lst.append(L[i][j])
			else:
				count = count + 1
	if count == 1:
		return True
	else:
		return False
print(hasduplicates([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 11]]))