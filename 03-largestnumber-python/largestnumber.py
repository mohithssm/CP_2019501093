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
        return None

print(fun_largestnumber("we have 32 dogs 3 cats"))