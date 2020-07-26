# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
    count = 1
    while n>= 0:
        if isTidy(count):
            n = n - 1
        count = count + 1
    return count - 1

def isTidy(num):
    st = str(num)
    for i in range(len(st)-1):
        if st[i] > st[i+1]:
            return False
    return True
