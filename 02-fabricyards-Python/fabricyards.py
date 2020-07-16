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
	# your code goes here
	yard = 36
	if inches == 0 or inches == 36:
		return 0
	elif 0 < inches < yard:
		return 1
	elif inches > 36:
		return 3

def fun_fabricexcess(inches):
	# your code goes here
	return 1


