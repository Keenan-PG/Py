'''
CLI / REPL Calculator
'''

userInput1 = int(input("What is the first number of your calculation? "))                           # taking first input - casted as an int 
userInput2 = int(input("What is the second number of your calculation? "))                          # taking second input - casted as an int
calculation = str(input("Which calculation type would you like? (please type one of: +, -, *, / ")) # taking option of calculation in sense of +, -, *, /

'''
Conditional logic to return the relevant (selected) result.
'''

if calculation == "+":                                                                              # elseif statement checking calc type input - checking for +
    answer = (userInput1 + userInput2)                                                              # storing addition in answer var
elif calculation == "-":                                                                            # elseif statement checking calc type input - checking for -
    answer = (userInput1 + userInput2)                                                              # storing subtraction in answer var
    print ("The result of the subtraction between " + str(userInput1) + " and " + str(userInput2) + " is: " + str(answer))
elif calculation == "*":                                                                            # elseif statement checking calc type input - checking for *
    answer = (userInput1 * userInput2)                                                              # storing multiplication in answer var
    print ("The result of the multiplication between " + str(userInput1) + " and " + str(userInput2) + " is: " + str(answer))
elif calculation == "/":                                                                            # if statement checking calc type input - checking for /
    answer = (userInput1 / userInput2)                                                              # storing division in answer var
    print ("The result of the division between " + str(userInput1) + " and " + str(userInput2) + " is: " + str(answer))
else:
    print ("Please enter a valid calculation type.")                                                # Validation for wrong input

