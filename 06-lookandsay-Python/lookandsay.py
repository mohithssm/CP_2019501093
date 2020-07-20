# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	count = 0
	lst = []
	x = 0

	for i in range(len(a)):
		print(i)
		if a[i] == a[x]:
			count = count + 1
			# print("count is", count)
		else:
			# print("-------------------")
			x = i
			# print("x value", x)
			t1 = (count, a[i-1])
			lst.append(t1)
			# print(x)
			# print("count is", count)
			count = 0

	return (lst)
print(lookandsay([3,3,8,3,3,3,3]))	 