# Recursion-Only recursion_secondlargest(L) [15 pts]
# Note: recall that you may not use sort, sorted, min, or max this week! With that in mind, write the function 
# recursion_secondlargest(L) that takes a list of integers in any order and returns the second-largest value in the list. To 
# be more precise, it returns the second value from the end if the list was sorted (though you do not need to sort 
# it to solve this problem), so if the largest value occurs twice, you would return that value. Also, if there are 
# fewer than 2 values in the list, return None. Here are some test cases:
# assert(recursion_secondlargest([1,2,3,4,5]) == 4)
# assert(recursion_secondlargest([4,3]) == 3)
# assert(recursion_secondlargest([4,4,3]) == 4)
# assert(recursion_secondlargest([-3,-4]) == -4)
# assert(recursion_secondlargest([4]) == None)
# assert(recursion_secondlargest([ ]) == None)
# Again, you do not need to sort the list. We didn't sort it in our sample solution. We just tracked the two largest 
# values as we recursively traversed the list. Also, you may not use loops/iteration in this problem

def recursion_secondlargest(L):
	if len(L) < 2:
		return None
	else:
		s = sec_large(L)	

def sec_large(L):
	largest = L[0]
	largest_2nd = None

	for elem in L[1:]:
		if elem > largest:
			largest_2nd = largest
			largest = elem
		elif largest_2nd == None or largest_2nd < elem:
			largest_2nd = elem
	return largest_2nd
print(sec_large( [12, 45, 2, 41, 31, 10, 8, 6, 4] ))