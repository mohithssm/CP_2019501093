# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(a): 
	total = 0
	if len(a) == 0:
		return 0
	else:
		for i in range(len(a)):
			if i%2 == 0:
				total = total + a[i]
			else:
				total = total - a[i]
		return total

print(fun_alternatingsum([1, 2, 3, 4]))
