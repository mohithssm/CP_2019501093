# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	lst = []
	for i in range(len(L)):
		for j in range(len(L[i])):
			lst.append(L[i][j])

	for i in range(len(lst)):
		if lst[i] in lst:
			print(lst[i])
			return True
		else:
			return False

print(hasduplicates([[2, 7, 9], [9, 5, 1], [4, 3, 8]]))