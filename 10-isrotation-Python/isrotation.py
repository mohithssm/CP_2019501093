# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	x_st = str(x)
	print(x_st)
	temp = 0
	for i in range(len(x_st)):
		m = int(str(x)[i:] + str(x)[:i])
		print(m)
		temp = temp +  m
	if temp != y:
		return False
	else:
		return True

print(isrotation(3412, 1234))