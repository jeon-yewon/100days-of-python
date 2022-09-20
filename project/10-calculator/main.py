import art
from replit import clear

#Calculator
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2


def calculate(num1):
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    calc_result = calculation_function(num1, num2)
    print(f"✅{num1} {operation_symbol} {num2} = {calc_result}")
    return calc_result


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


# first calc
def start_calc():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    print("=== operation list ===")
    for symbol in operations:
        print(symbol)
    print("=====================")

    answer = calculate(num1)

    is_continue = True
    while is_continue:
        re_run = input(
            f"❗️Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        )
        if re_run == 'y':
            answer = calculate(answer)
        else:
            is_continue = False
            clear()
            start_calc()

start_calc()
