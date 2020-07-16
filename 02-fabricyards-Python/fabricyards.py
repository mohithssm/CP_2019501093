# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!


def fun_fabricyards(inches):
	if (inches == 0):
		return 0
		if (inches == 1 or inches < 36):
			return 1
		elif (inches % 36 == 0):
			return inches // 36 
	return (inches // 36) + 1

def fun_fabricexcess(inches):
	if inches == 0:
		return 0
	fab_v = fun_fabricexcess(inches)
	result = fab_v * 36 - inches
	return result


