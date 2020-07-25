# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
import math

def fun_is_smith_number(n):
    sumOfPrimeFactors = 0
    prime_factors = primeFactors(n)
    len_prime_factors = len(prime_factors)
    if len_prime_factors and prime_factors[len_prime_factors - 1] == n:
        prime_factors.pop()
    for elem in prime_factors:
        sumOfPrimeFactors = sumOfPrimeFactors + fun_sum_of_digits(temp)
    
    if sumOfPrimeFactors == fun_sum_of_digits(n):
        return True
    else:
        return False

def fun_sum_of_digits(n):
    sum = 0
    while n != 0:
        rem = num % 10
        sum = sum + rem
        n = n // 10
    return sum

def fun_prime_factors(n):
    j = 2
    facotrs_lst = []
    while j*j <= n:
        if n % j:
            j = j + 1
        else:
            n = n // j
            facotrs_lst.append(j)
    if n > 1:
        facotrs_lst.append(n)
    return facotrs_lst

def fun_nth_smithnumber(n):
    count = -1
    temp = 4
    while True:
        if fun_is_smith_number(temp):
            count = count + 1
            if count == n:
                return temp
        temp = temp + 1


