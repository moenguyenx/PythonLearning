from art import logo
from clearconsole import clearconsole


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    should_continue = True
    print(logo)
    num1 = float(input("Please enter num1: "))
    for symbol in operations:
        print(symbol)

    while should_continue:
        symbol = input("Choose symbol: ")
        next_num = float(input("Please enter next number: "))
        calculation_function = operations[symbol]
        answer = calculation_function(num1, next_num)
        print(f"{num1} {symbol} {next_num} = {answer}")

        proceed = input("Type 'y' to continue or 'n' to restart: ").lower()
        if proceed == 'y':
            num1 = answer
        else:
            should_continue = False
            clearconsole()
            calculator()


calculator()
