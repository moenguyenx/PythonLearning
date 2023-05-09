# Caesar Cipher
from art import logo
from art import alphabet

print(logo)


def caesar(plain_text, shift_amount, direct):
    cipher_text = ""
    if direct == 'decode':
        shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The {direct}d message is: {cipher_text} ")


proceed_program = True
while proceed_program:
    direction = input("Enter 'encode' to encode or 'decode' to decode message...\n")
    text = input("Type your message: \n").lower()
    shift = int(input("Enter shift number: \n"))
    shift = shift % 26
    caesar(text, shift, direction)
    terminate = input("Do you want to continue? 'yes' or 'no' \n")
    if terminate == 'no':
        proceed_program = False
        print("Goodbye!")
