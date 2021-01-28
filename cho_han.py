import random
from setup import *

def play_cho_han(guess, bet):
    if bet <= 0:
        return bet_zero

    divider()
    print("Let's play Cho-Han!")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("The sum of the two dice is " + str(total))

    if guess == "Even" and total % 2 == 0:
        return bet_outcome_win(bet)
    elif guess == "Odd" and total % 2 == 1:
        return bet_outcome_win(bet)
    else:
        return bet_outcome_lost(bet)