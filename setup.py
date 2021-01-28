def divider():
    print("------------------")

def print_text(text):
    print(text)
    divider()

def is_bet_zero():
    divider()
    print_text("Your bet should be above 0.")
    return 0

# status is won or lost
def bet_outcome_win(bet):
    print_text("You won " + str(bet) + " dollars!")
    divider()
    return bet

def bet_outcome_lost(bet):
    print_text("You lost " + str(bet) + " dollars!")
    divider()
    return -bet
