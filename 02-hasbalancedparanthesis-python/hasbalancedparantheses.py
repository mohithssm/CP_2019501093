def fun_hasbalancedparantheses(a):
    count = 0
    for elem in a:
        if elem == '(':
            count = count + 1
        elif elem == ')':
            count = count - 1
    
    return count == 0

print(fun_hasbalancedparantheses("( ( ( ( )3)))  "))