# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):

	count = 1
	lst = []
	if len(a) == 0:
		return a
	else:
		for i in range(len(a)-1):
			if a[i] == a[i+1]:
				print(count)
				
				count = count + 1

				# print(a[i], count)
			else:
				lst.append((count, a[i]))
				count = 1
		return (lst)

print(lookandsay([3,3,8,3,3,3,3]))