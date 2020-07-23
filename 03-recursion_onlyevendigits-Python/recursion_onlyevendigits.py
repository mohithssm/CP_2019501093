# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l):
	if l == []:
		return []
	else:
		res = fun_checkeven(l)
		return res
		# return fun_recursion_onlyevendigits(l[0]) + fun_recursion_onlyevendigits(l[1:])

def fun_checkeven(l):
	lst_len = len(l)
	lst = []
	mainLst = []
	for i in range(len(l)):
		rev = 0
		rev2 = 0
		while l[i] > 0:
			r = l[i] % 10
			if r%2 == 0:
				rev = (rev*10) + r
			l[i] = l[i] // 10
		lst.append(rev)
	
	for j in range (len(lst)):
		while lst[j] > 0:
			rem = lst[j] % 10
			rev2 = (rev2*10) + rem
			lst[j] = lst[j] // 10
		mainLst.append(rev2)
	return mainLst
print(fun_recursion_onlyevendigits([43, 23265, 17, 58344]))