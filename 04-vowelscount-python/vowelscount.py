def vowelscount(n):
    arr = []
    count = 0
    small_vowels = "aeiou"
    capital_vowels = "AEIOU"
    for elem in n:
        if elem in small_vowels or elem in capital_vowels:
            count = count + 1
    return count
