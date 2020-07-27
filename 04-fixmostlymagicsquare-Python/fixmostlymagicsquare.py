# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	r = [sum(elem) for elem in L]
	c = [0] * len(L)
	for i in range(len(L)):
		for j in range(len(L)):
			c[j] = c[j] + L[i][j]
	for elem in r:
		if r.count(elem) > 1:
			val = elem
		elif r.count(elem) == 1:
			odd = elem
	x1 = r.index(odd)
	x2 = c.index(odd)
	L[x1][x2] = L[x1][x2] - (odd - val)
	return L