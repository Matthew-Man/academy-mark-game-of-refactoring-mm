import random
from setup import *

def play_coin_flip(guess, bet):
    if bet <= 0:
        return bet_zero()

    #Starts the game and flips the coin
    divider()
    print("Let's flip a coin! You guessed " + guess)
    result = random.randint(1,2)

    # Prints the result of the coin flip. A 1 is heads, a 2 is tails
    if result == 1:
        print("Heads!")
    elif result == 2:
        print("Tails")

    # Determines if you won or lost and returns either bet or -bet
    if (guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
        return bet_outcome_win(bet)
    else:
        return bet_outcome_lost(bet)