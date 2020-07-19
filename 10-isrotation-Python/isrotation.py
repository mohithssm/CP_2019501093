# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	x_st = str(x)
	arr = []
	for i in range(len(x_st)):
		m = int(str(x)[i:] + str(x)[:i])
		# print(m)
		arr.append(m)
	print(arr)
	if y in arr:
		return True
	else:
		return False

print(isrotation(3412, 1234))