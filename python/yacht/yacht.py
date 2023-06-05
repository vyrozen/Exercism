# Score categories.
# Change the values as you see fit.
YACHT = lambda dice : 50 if (len(set(dice)) == 1) else 0
ONES = lambda dice : dice.count(1)*1
TWOS = lambda dice : dice.count(2)*2
THREES = lambda dice : dice.count(3)*3
FOURS = lambda dice : dice.count(4)*4
FIVES = lambda dice : dice.count(5)*5
SIXES = lambda dice : dice.count(6)*6
FULL_HOUSE = lambda dice : sum(dice) if len(set(dice)) == 2 and any(dice.count(n) == 3 for n in [1,2,3,4,5,6]) else 0
FOUR_OF_A_KIND = lambda dice : FOUR_OF_A_KIND(dice)
LITTLE_STRAIGHT = lambda dice : 30 if dice == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda dice : 30 if dice == [2,3,4,5,6] else 0
CHOICE = lambda dice : sum(dice)

def FOUR_OF_A_KIND(dice) : 
    if (dice[0] == dice[3]) : return(4*dice[0])
    elif (dice[1] == dice[4]) : return(4*dice[1])
    else : return (0)

def score(dice, category):
    return category(sorted(dice))
    pass
