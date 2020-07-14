# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	s1 = (y2-y1)/(x2-x1)
	s2 = (y3-y2)/(x3-x2)
	s3 = (y3-y1)/(x3-x1)

	if (s1 * s2 == -1 ):
		return True
	elif (s2 * s3 == -1):
		return True
	elif (s1 * s3 == -1):
		return True
	else:
		return False


	