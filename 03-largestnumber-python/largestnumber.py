import math
def fun_largestnumber(a):
    m = 0
    n = 0
    for i in range(len(a)):
        c = a[i]
        if c >= "0" and c <= "9":
            n = n * 10 + int(int(c) - 0)
        else:
            m = max(m , n)
            n = 0

    return max(m, n)
