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

# Function to approximate the square root using Newton's method
def squareroot(input_nr):
    epsilon = 0.1  # Define the precision threshold for the approximation
    k = input_nr  # Store the original input number
    guess = k / 2.0  # Start with an initial guess (half of the input number)

    # Iteratively refine the guess until the difference is within the defined precision
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (guess ** 2 - k) / (2 * guess)  # Apply Newton's method formula

    return guess  # Return the approximated square root

# Function to get valid user input (positive float)
def user_inputfloat(): 
    while True:  # Keep prompting until a valid input is received
        try:
            amount_1 = float(input("Please enter a positive value = "))  # Get user input and convert to float

            if amount_1 > 0:  # Ensure the input is a positive number
                break  # Exit the loop if the input is valid
            else:
                print("Your input is invalid, please enter a positive value - ")  # Error message for negative input

        except:
            print("Your input is invalid, please enter a positive value - ")  # Handle non-numeric inputs

    return amount_1  # Return the valid input number

# Get user input for the number to find the square root of
input_nr = user_inputfloat()

# Compute square root using Newton's approximation method
sqr = squareroot(input_nr)

# Print results: Newton's method approximation vs. Python's built-in sqrt function & using f string
print(f"Using the Newton approximation method - the squareroot of {input_nr} = {sqr}")
print(f"Using the in-built Python math module - the squareroot of {input_nr} = {math.sqrt(input_nr)}")

'''
Resources:
The following resources were used in completing this task:
1. Literature on how Newton's method works (forumula's included) - https://en.wikipedia.org/wiki/Newton%27s_method
2. How to implement the Newton method in python - https://github.com/kgisl/pythonFDP/blob/master/manual/lab2-kgashok.py.md
3. Python math module to check Newton method results vs in-build library - https://www.w3schools.com/python/python_math.asp
'''