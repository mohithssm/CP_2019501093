# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

# def fun_recursion_onlyevendigits(l):
# 	if l == []:
# 		return []
# 	else:
# 		for i in range(len(l)):
# 			res = fun_checkeven(l[i])
# 		return res
def fun_checkeven(ele):
	lst = []
	rev = 0
	while ele > 0:
		r = ele % 10
		if r%2 == 0:
			rev = (rev*10) + r
		ele = ele // 10
	lst.append(rev)
	
	for j in range (len(lst)):
		rev2 = 0
		while lst[j] > 0:
			r = lst[j] % 10
			rev2 = (rev2*10) + r
			lst[j] = lst[j] // 10
	return rev2

# print(fun_recursion_onlyevendigits([5, 0 , 66, 82, 121]))
print(fun_checkeven(234))