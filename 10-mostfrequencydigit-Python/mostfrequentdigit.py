# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
from collections import Counter

def mostfrequentdigit(n):

	n = [num for num in str(n)]
	n.sort()
	l = (dict(Counter(n)))
	max_key = max(l, key = l.get)
	return max_key	

print(mostfrequentdigit(5231123123123))
print(mostfrequentdigit(5312312355565))
print(mostfrequentdigit(2))

