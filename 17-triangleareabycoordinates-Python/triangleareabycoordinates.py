# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
import math

def trianglearea(s1, s2, s3):
	s = (s1 + s2 + s3)/2
	area = math.sqrt((s) * (s-s1) * (s-s2) * (s-s3))
	return area

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	l = math.sqrt(((y2-y1)**2) + ((x2-x1)**2))
	m = math.sqrt(((y3-y2)**2) + ((x3-x2)**2))
	n = math.sqrt(((y3-y1)**2) + ((x3-x1)**2))
	return trianglearea(l, m, n)
