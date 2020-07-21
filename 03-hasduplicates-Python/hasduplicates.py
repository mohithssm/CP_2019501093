# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	lst = []
	for i in range(len(L)):
		for j in range(len(L[i])):
			if L[i][j] not in lst:
				lst.append(L[i][j])
				return False
			else:
				return True
	print(lst)
print(hasduplicates([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))