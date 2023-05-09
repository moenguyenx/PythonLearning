# Tip calculator

print("-----Welcome to the tip calculator-----")

bill = float(input("How much was your bill? "))

tip = int(input("How much tip(%) would you like to give? "))

people = int(input("How many people to split the bill? "))

# billPerPerson = round(bill*(1 + tip/100)/people, 2)
billPerPerson = "{:.2f}".format(bill * (1 + tip / 100) / people)

print(f'Each person should pay: {billPerPerson}')
