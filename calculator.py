# This program will add, subtract, multiply, and divide
import sys               # imports the sys library so i can do sys.ext()

def add(x, y):           # function to do addition
    return x + y

def subt(x, y):          # function  for subtraction
    return x - y

def mult(x, y):          # function for multiplication
    return x * y

def divide(x, y):        # function for division
    return x / y

operators = ['+', '-', '*', '/']                           # list of operators the user can use

while True:                                                # main loop so user can start over if they want

    while True:                                            #loop to get first number. checks to make sure its a float
        try:
            num_1 = float(input('Enter a number: '))
        except:
            print('This is not a number. Please Try again')
            continue                                       # if it isn't a float it goes back to the start of this loop
        else:
            break

    while True:                                            # loop to get user input. Checks to make sure they type in + - * /
        operator_1 = input('What operator would you like to use? +, -, *, or /: ')
        if operator_1 not in operators:
            print('This is not one of your choices')
            continue
        else:
            break

    while True:                                            # loop to get 2nd number. checks to makre sure its a float
        try:
            num_2 = float(input('Enter another number: '))
            if (operator_1 == '/') and (num_2 == 0):
                print('You cannot divide by 0')
                continue
        except:
            print('This is not a number. Please Try again')
            continue
        else:
            break

# Calls the proper operator function and does the calculations.  Shows the answer.
    if operator_1 == '+':
        print('The total is: ', add(num_1, num_2))

    elif operator_1 == '-':
        print('The total is: ', subt(num_1, num_2))

    elif operator_1 == '*':
        print('The total is: ', mult(num_1, num_2))

    elif operator_1 == '/':
        print('The total is: ', divide(num_1, num_2))

    while True:                                             # Loop to see if user wants to make another calculation
        more_operations = input('Would you like to do another calculation? Y or N: ')
        if more_operations == 'Y':
            break
        elif more_operations == 'N':
            sys.exit()
        else:
            print('That was not a choice')
            continue

    continue


