# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	x1 = digits_lst(x)
	y1 = digits_lst(y)
	print(x1)
	print(y1)




def digits_lst(elem):
	lst = []
	while elem > 0:
		rem  = elem % 10
		lst.append(rem)
		elem = elem // 10
	return lst[::-1]

print(fun_carrylessadd(785, 376))