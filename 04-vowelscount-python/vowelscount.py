def vowelscount(S):
    arr = []
    count = 0
    owels = "aeiou"
    for elem in S:
        if elem in owels:
            count = count + 1
    return count