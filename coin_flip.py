import random

def divider():
    print("------------------")

def print_text(text):
    print(text)
    divider()

def play_coin_flip(guess, bet):
    #Makes sure your bet was above 0
    if bet <= 0:
        divider()
        print_text("Your bet should be above 0.")
        return 0

    #Starts the game and flips the coin
    print("------------------")
    print("Let's flip a coin! You guessed " + guess)
    result = random.randint(1,2)

    # Prints the result of the coin flip. A 1 is heads, a 2 is tails
    if result == 1:
        print("Heads!")
    elif result == 2:
        print("Tails")

    # Determines if you won or lost and returns either bet or -bet
    if (guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
        print_text("You won " + str(bet)+" dollars!")
        return bet
    else:
        print_text("You lost " + str(bet)+" dollars!")
        return -bet