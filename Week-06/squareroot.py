'''
Assignment summary:
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 

'''
# squareroot.py
# author - Hugo van Zyl
import math #import math library for access to built in math functions (to check the answer of my custom function)

def squareroot (input_nr):
    epsilon = 0.01
    k       = input_nr
    guess   = k / 2.0

    while abs(guess * guess - k) >= epsilon:
        guess = guess - (guess ** 2 - k) / (2 * guess)
    return guess

while True: # run this while loop at start of program
    try: # do following code and check for errors
        amount_1 = float(input("Please enter a positive value = ")) # get user input and convert to float
        if amount_1 > 0: # if the input amount is > 0 exit this loop
            break # exit loop
        else: # if above not valid, show error message
            print("Your input is invalid, please enter a positive value - ") # display error message and loop will start over again
            
    except: # reprompt for input if input is invalid
        print("Your input is invalid, please enter a positive value - ") # display error message and loop will start over again

sqr = squareroot(amount_1)

print(f"Using the Newton approximation method - the squareroot of {amount_1:.3} = {sqr}")
print(f"Using the in-built Python math module - the squareroot of {amount_1:.3} = {math.sqrt(amount_1)}")

'''
Resources:
The following resources were used in completing this task:
1. Literature on how Newton's method works (forumula's included) - https://en.wikipedia.org/wiki/Newton%27s_method
2. How to implement the Newton method in python - https://github.com/kgisl/pythonFDP/blob/master/manual/lab2-kgashok.py.md
3. Python math module to check Newton method results vs in-build library - https://www.w3schools.com/python/python_math.asp
'''