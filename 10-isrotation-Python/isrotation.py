# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	lst1 = []
	lst2 = []

	while x > 0:
		rem1 = x % 10
		x = x // 10
		lst1.append(rem1)
	while y > 0:
		rem2 = y % 10
		y = y // 10
		lst2.append(rem2)

	return (lst1, lst2)

print(isrotation(3412, 1234))