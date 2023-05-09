# The number guessing game

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from random import randint

HARD_LEVEL = 5
EASY_LEVEL = 10


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"\nYou got it! the answer is {answer}")


def set_difficulty():
    level = input("What level do you want to play? 'easy' or 'hard'\n").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(logo)
    print("-----Welcome to the number guessing game-----")
    print("I'm thinking of a number between 1 to 20.")
    answer = randint(1, 20)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess ")
        guess = int(input("Please make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've ran out of attempt")
            return
        elif guess != answer:
            print("Guess again.\n")

game()

