# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    st = ""
    if s1 == "" or s2 == "":
        return None
    for i in range(len(s1)):
        for j in range(i, len(s1) + 1):
            subSt = s1[i:]
            if subSt in s2:
                if len(subSt) > len(st):
                    st = subSt
                elif len(subSt) < len(st):
                    if subSt < st:
                        st = subSt
    return st


print(longestcommonsubstring("abcdef", "abqrcdest"))