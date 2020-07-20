# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	dict = {}
	for elem in s:
		if elem in dict:
			dict[elem] = dict[elem] + 1
		else:
			dict[elem] = 1
		
	result = sorted(dict.items(), key = lambda l : l[1], reverse = True)
	return result[n-1][0]


