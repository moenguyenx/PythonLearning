# The Hangman Game
import random
import hangmanASCII
import hangmanWORD

print(hangmanASCII.logo)


lives = 6
chosen_word = random.choice(hangmanWORD.word_list)
print(f'The mistery word has {len(chosen_word)} digits')
print(f'Pssst, the solution is {chosen_word}.')
display = []

for _ in range(len(chosen_word)):
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Please make a guess :>  \n").lower()

    if guess in display:
        print(f'You have already guessed {guess}')

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = guess

    if guess not in chosen_word:
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangmanASCII.stages[lives])

