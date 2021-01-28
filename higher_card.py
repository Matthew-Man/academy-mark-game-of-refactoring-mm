import random
from setup import *

def play_higher_card(bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        bet_zero()

    # Draws two cards between 1 and 10 and prints the result
    print("------------------")
    print("Let's play a game of cards!")
    mine = random.randint(1, 10)
    theirs = random.randint(1, 10)
    print("Your card was " + str(mine))
    print("Their card was " + str(theirs))

    #Determines who won and returns either bet, -bet or 0 (in the case of a tie.)
    if mine > theirs:
        print("You won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    elif mine < theirs:
        print("You lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet
    else:
        print("It was a tie!")
        print("------------------")
        return 0