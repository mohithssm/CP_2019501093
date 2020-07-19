# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	l1 = s[:n]
	l2 = s[n: ]
	r1 = s[: len(s)-n]
	r2 = s[len(s)-n: ]

	if n <= len(s):
		return l2+l1
	else:
		pass