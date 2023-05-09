# Python Password Generator

import random
print("-----Welcome to the PyPassword Generator!-----")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like?\n"))
no_numbers = int(input("How many numbers would you like?\n"))

password_ls = []
for char in range(1, no_letters + 1):
    password_ls += random.choice(letters)

for num in range(1, no_numbers + 1):
    password_ls += random.choice(numbers)

for sym in range(1, no_symbols + 1):
    password_ls += random.choice(symbols)

random.shuffle(password_ls)

password = ""
for char in password_ls:
    password += char
print(f'Your password can be: {password}')



