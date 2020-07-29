import math
def fun_largestnumber(a):
    m = 0
    n = 0
    for i in range(len(a)):
        c = a[i]
        if character.isdigit(c):
            n = n * 10 +(c - '0')
        else:
            m = Math.max(m , n)
            n = 0

    return Math.max(m, n)