def vowelscount(n):
    arr = []
    count = 0
    owels = "aeiou"
    for elem in n:
        if elem in owels:
            count = count + 1
    return count