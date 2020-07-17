# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	l = []
	lst = list(text)
	for i in range(len(lst)):
		for j in range(len(lst)):
			if lst[j] not in lst[i]:
				l.append(lst[i])
	return "".join(l)
print(removeduplicate("JavaPython"))