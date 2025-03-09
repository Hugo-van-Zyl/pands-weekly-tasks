'''
Assignment summary:
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

'''
# collatz.py
# author - Hugo van Zyl
while True: # run this while loop at start of program
    try: # do following code and check for errors
        amount_1 = int(input("Please enter a positive integer = ")) # get user input and convert to integer
        if amount_1 > 0: # if the input amount is > 0 exit this loop
            break # exit loop
        else: # if above not valid, show error message
            print("Your input is invalid, please enter a positive integer - ") # display error message and loop will start over again
            
    except: # reprompt for input if input is invalid
        print("Your input is invalid, please enter a positive integer - ") # display error message and loop will start over again

print(amount_1," ", end="") # print the number from the user input

while amount_1 != 1:  # run loop while amount_1 is not equal to 1

    if amount_1 % 2 == 0: # if input number is even, do the following
        amount_1 = int(amount_1/2) # apply collatz formula for even number
        #print(amount_1," ")
    elif amount_1 % 2 != 0: # if input number is odd, do the following
        amount_1 = int(amount_1*3 + 1) # apply collatz formula for odd number
        #print(amount_1," ")
    print(amount_1," ", end="") # print answer and set end="" to prevent each answer from being shown seperately on a new line

        

'''
Resources:
The following resources were used in completing this task:
1. Week04 Lecture videos
2. How to stop print function from printing on new line - https://www.datacamp.com/tutorial/python-print-without-new-line
3. Error handling - https://www.w3schools.com/python/python_try_except.asp
'''