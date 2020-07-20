# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):

	if n > 0:
		s_length = len(s)
		n =  n % s_length
		return s[s_length:] + s[:s_length]
	else:
		n = abs(n) % s_length
		return s[s_length - n: ] + s[ : s_length-n]