
from calculator_art import logo


# functions for mathematical operations
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# list containing operation symbols as keys and the functions as values
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }


def calculator():
    print(logo)

    num1 = float(input("\nWhat's the first number: "))
    for key in operations:  # loop through the operations list to display the symbols to user
        print(key)

    continue_calculating = True

    while continue_calculating:
        operation_choice = input("Which operation would you like to perform: ")
        num2 = float(input("What's the next number: "))
        calculation_function = operations[operation_choice]  # uses the operation chosen by the user as the key in the operations list
                                                             # and stores it as calculation_function
        answer = calculation_function(num1, num2)            # then uses calculation_function to calculate the answer by passing num1
                                                             # and num2 as parameters to the appropriate function in operations list

        print(f"\n{num1} {operation_choice} {num2} = {answer}")

        if input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start again: ") == 'y': #  asks user if they wish to continue
            num1 = answer
        else:
            continue_calculating = False
            calculator()  # calculator function calls itself to restart the program


# Program start
calculator()
