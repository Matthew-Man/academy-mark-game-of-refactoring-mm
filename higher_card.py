import random
from setup import *

def play_higher_card(bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        return bet_zero()

    # Draws two cards between 1 and 10 and prints the result
    divider()
    print("Let's play a game of cards!")
    mine = random.randint(1, 10)
    theirs = random.randint(1, 10)
    print("Your card was " + str(mine))
    print("Their card was " + str(theirs))

    #Determines who won and returns either bet, -bet or 0 (in the case of a tie.)
    if mine > theirs:
        bet_outcome_win(bet)
    elif mine < theirs:
        bet_outcome_lost(bet)
    else:
        print("It was a tie!")
        print("------------------")
        return 0