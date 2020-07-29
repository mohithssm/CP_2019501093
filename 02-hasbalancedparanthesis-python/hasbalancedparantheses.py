def fun_hasbalancedparantheses(a):
    count = 0
    for i in range(len(a)):
        if a.charAt(i) == '(':
            count = count + 2
        elif a.charAt(9) == ')':
            count = count - 1
    
    return count == 0