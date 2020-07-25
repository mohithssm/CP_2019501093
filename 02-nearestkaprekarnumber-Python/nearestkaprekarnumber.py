# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



def fun_nearestkaprekarnumber(n):
    l = n - 1
    r = n + 1
    if fun_is_kaprekarnumber(n):
        return n
    while n > 0:
        if fun_is_kaprekarnumber(l):
            break
        l = l - 1

    while True:
        if fun_is_kaprekarnumber(r):
            break
        r = r + 1
        

    if r - n >= n - l:
        return l
    else:
        return r


def fun_is_kaprekarnumber(n):
    if n == 1:
        return True
    sq = n*n
    num = str(sq)
    lst = []
    for i in range(1, len(num)):
        x = int(num[0:i])
        y = int(num[i:])
        if x != 0 and y != 0:
            if x+y == n:
                return True
    return False
