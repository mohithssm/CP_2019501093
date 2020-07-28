# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

import string
import collections

def leastfrequentletters(s):
	freqletters = []
	leastfreqletters = []
	letters_list = list(string.ascii_lowercase)
	s = s.lower()
	for elem in s:
		if elem in letters_list:
			freqletters.append(elem)
	counter = collections.Counter(freqletters)
	print(counter.keys())
	print(counter.values())

print(leastfrequentletters("aDq efQ? FB'daf!!!"))