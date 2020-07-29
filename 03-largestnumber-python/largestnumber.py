import math
def fun_largestnumber(a):
    ls = list()
    for elem in a.split():
        try:
            ls.append(int(elem))
        except:
            pass
    try:
        return max(ls)
    except:
        return 0

print(fun_largestnumber("we have dogs cats"))