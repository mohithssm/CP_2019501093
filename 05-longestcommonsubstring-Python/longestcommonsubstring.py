# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

from difflib import SequenceMatcher

def longestcommonsubstring(s1, s2):
    seqMatch = SequenceMatcher(None, s1, s2)
    a = 0
    b = 0 
    m = seqMatch.find_longest_match(a, len(s1), b, len(s2))

    if (m.size != 0):
        res = s1[m.a: m.a + m.size]
        print(res)
        return res
    else:
        return None

print(longestcommonsubstring("abcdef", "abqrcdest"))