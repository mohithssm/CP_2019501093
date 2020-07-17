# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	result = []
	lst = list(text)
	for elem in lst:
		if elem not in result:
			result.append(elem)
	return "".join(result)
print(removeduplicate("JavaPython"))