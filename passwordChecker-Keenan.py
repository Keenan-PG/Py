'''
CLI / REPL Password checker
'''

actualPass = "Keenan1998"                                                       # setting password to test against
userName = str(input("What is your username? "))                                # taking userName input
password = str(input("Hello " + userName + "! What is your password? "))        # taking password input

'''
Conditional logic to return the validated result
'''

if password == actualPass:                                                      # testing if inputted password is the same as actualPassword
    print("Password is correct! Come on in " + userName + "!")                  # returning result for true condition (password matches)
else:
    print("Password is wrong :( Au revoir).")                                   # returning result for false condition (password doesn't match)
                                            

