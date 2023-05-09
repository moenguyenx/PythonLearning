# The secret auction program
from clear import clear
from art import logo

print(logo)
# HINT: You can call clear() to clear the output in the console.

end_auction = False
participant = {}


def find_winner():
    max_bid = 0
    winner = ""
    for bidder in participant:
        bid_amount = participant[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f"The winner is '{winner}'  with ${max_bid}")

while not end_auction:
    name = input("Please enter your name: \n")
    bid = int(input("How much do you want to bid? $"))
    participant[name] = bid

    proceed = input("Is there anyone else want to bid? yes or no\n").lower()
    if proceed == "no":
        end_auction = True
        find_winner()
    elif proceed == "yes":
        clear()
