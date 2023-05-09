# Higher Lower game

from art import logo, vs
from game_data import data
from clearconsole import clearconsole
import random


def get_random_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    follower = account["follower_count"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"


def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        guess = input("Who has more followers? 'A' or 'B'\n").lower()
        is_correct = check_answer(guess, account_a["follower_count"], account_b["follower_count"])

        clearconsole()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print("You fucked up!")


game()
