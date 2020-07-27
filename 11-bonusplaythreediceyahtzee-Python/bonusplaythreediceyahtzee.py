# bonusPlayThreeDiceYahtzee(dice) [5pts]
# In this exercise, we will write a simplified form of the dice game Yahtzee. In this version, the 
# goal is to get 3 matching dice, and if you can't do that, then you hope to at least get 2 
# matching dice. The game is played like so:
# Roll 3 dice.
# If you do not have 3 matching dice:
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# Otherwise, if you have no matching dice, keep the highest die and roll two dice to replace the 
# other two dice.
# Repeat step 2 one more time.
# Finally, compute your score like so:
# If you have 3 matching dice, your score is 20 + the sum of the matching dice.
# So if you have 4-4-4, your score is 20+4+4+4, or 32.
# If you only have 2 matching dice, your score is 10 + the sum of the matching dice.
# So if you have 4-4-3, your score is 10+4+4, or 18.
# If you have no matching dice, your score is the highest die.
# So if you have 4-3-2, your score is just 4.
# Our goal is to write some Python code that plays this game. It's a large task, so we will use 
# top-down design and break it up into smaller, more manageable pieces. So we'll first write some 
# helper functions that do part of the work, and then those helper functions will make our final 
# function much easier to write. 

# Also note: we will represent a hand of 3 dice as a single 3-digit integer. So the hand 4-3-2 will 
# be represented by the integer 432. With that, let's start writing some code. Be sure to write 
# your functions in the same order as given here, since later functions will make use of earlier 
# ones!

# we've made it to the last function: bonusPlayThreeDiceYahtzee(dice), the function that actually earns 
# the 2.5 bonus points! This function takes one value, the dice with all the rolls for a game of 3-Dice 
# Yahtzee. The function plays the game -- it does step1 and gets the first 3 dice (from the right), then it 
# does step2 twice (by calling playStep2, which you already wrote), and then it computes the score (by 
# calling score, which you already wrote). The function should return two values -- the resulting hand 
# and the score for that hand. For example:
# assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
# assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
# assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
# assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
# assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
# assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))


def bonusplaythreediceyahtzee(dice):
	dice = str(dice)
	x = int(dice[:4])
	y = int(dice[4:])
	y, x = playstep2(y, x)
	y, x = playstep2(y, x)
	return y, score(y)

def score(hand):
	(x, y, z) = handToDice(hand)
	if x != y and y != z and z != x:
		x = max(x, y, z)
		return x
	elif x == y and y == z and z == x:
		return 20 + x + y + z
	elif x == y:
		return 10 + x + y
	elif y == z:
		return 10 + y + z
	elif x == z:
		return 10 + x + z	


def playstep2(hand, dice):
	(x, y, z) = handToDice(hand)
	if x != y and y != z and z != x:
		x = max(x, y, z)
		y = dice % 10
		dice = dice // 10
		z = dice % 10
		dice = dice // 10
	else:
		if y == z:
			x = y
		elif x == z:
			y = x
		z = dice % 10
		dice = dice // 10
	hand = diceTo(x, y, z)
	return hand, dice

def handToDice(hand):
	st = str(hand)
	return int(st[0]), int(st[1]), int(st[2])

def diceTo(x, y, z):
	max_i = max(x, y, z)
	min_i = min(x, y, z)
	mid = (x + y + z) - (max_i + min_i)
	res = (max_i * 100) + (mid * 10) + min_i
	return res