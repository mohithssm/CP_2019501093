# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	st1 = str1[::-1]
	st2 = str2[::-1]
	for i in range (len(str1)):
		if( (str2[i:] + str2[:i]) == str1 or (str1[i:] + str1[:i]) == str2):
			return True

	if st1 == str2 and st2 == str1:
		return True
	else:
		return False