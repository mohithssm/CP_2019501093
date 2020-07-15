# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	nums = []
	if digit > 0:

		while (digit > 0):
			num  = digit % 10
			digit = digit // 10
			nums.append(num)
		if (k >= len(nums)):
			return 0
		else:
			return nums[k]
	else: 
		digit = -(digit)

		while (digit > 0):
			num  = digit % 10
			digit = digit // 10
			nums.append(num)
		if (k >= len(nums)):
			return 0
		else:
			return nums[k]