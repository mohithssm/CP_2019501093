# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.


def fun_nth_uglynumber(n):
    count = 1
    while n>= 0:
        if mDiv(count):
            n = n - 1
        count = count + 1
    return count - 1


def factors(num):
    num = mDiv(num, 2)
    num = mDiv(num, 3)
    num = mDiv(num, 5)
    return n == 1

def mDiv(num, i):
    while num % i == 0:
        num = num // i
    return num

