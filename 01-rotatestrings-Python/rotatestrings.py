# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	arr = []
	for i in range(len(s)):
		m = (str(s)[i:] + str(s)[:i])
		arr.append(m)
	if n in arr:
		return True
	else:
		return False

