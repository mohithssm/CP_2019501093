# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	result = []
	index = 0
	while True:
		pos = s1.find(s2, s2[0] )
		if pos == -1:
			result.append(s1[i:])
			return "".join(result)	
		else:
			result.append(s1[index:pos])
			result.append(s3)
			index = pos + len(s2)
