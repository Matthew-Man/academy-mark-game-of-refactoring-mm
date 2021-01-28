import random
from coin_flip import play_coin_flip
from higher_card import play_higher_card
from cho_han import play_cho_han
from roulette import play_roulette

total = 100

total += play_coin_flip("Heads", 10)
total += play_higher_card(5)
total += play_cho_han("Even", 2)
total += play_roulette("Even", 10)
total += play_roulette(3, 1)
total += play_roulette("Odd", total)
print("Your total amount of money is " + str(total))
