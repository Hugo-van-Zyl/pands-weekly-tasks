'''
Assignment summary:
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

'''
# accounts.py
# author - Hugo van Zyl
while True:
    try:
        amount_1 = int(input("Please enter a positive integer = "))
        if amount_1 > 0:
            break
        else:
            amount_1 = int(input("Please enter a positive integer = "))
            
    except:
        print("Your input is invalid, please enter a positive integer - ")

print(amount_1," ", end="")

while amount_1 != 1:  

    if amount_1 % 2 == 0:
        amount_1 = int(amount_1/2)
        #print(amount_1," ")
    elif amount_1 % 2 != 0:
        amount_1 = int(amount_1*3 + 1)
        #print(amount_1," ")
    print(amount_1," ", end="")

        #elif amount_1 == 1:
        #    break #exit loop if input valid
        

'''
Resources:
The following resources were used in completing this task:
1. Week04 Lecture videos
2. How to stop print function from printing on new line - https://www.datacamp.com/tutorial/python-print-without-new-line
3. Error handling - https://www.w3schools.com/python/python_try_except.asp

'''