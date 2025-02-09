#bank.py
'''
The script aims to:

1. Prompt the user and read in two money amounts (in cent)
2. Add the two amounts
3. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount

'''
#author: Hugo van Zyl

while True: #use while loop to iterate through input until the user has inputted a valid integer for amount_1 i.e. to prevent errors from strings, decimals etc
    try: #test below for errors
        amount_1 = int(input("Enter first amount in cents - ")) #define variable and equal to user input. Use int() function to convert standard string input to a integer. This will be later needed for sum operation
        break #exit loop if input valid
    except ValueError: #do the below if input is invalid
        print("Your input is invalid, please enter a whole number in cents - ") #promt the user to re-input as previous input was invalid

while True: #use second while loop for amount_2 otherwise program will re-ask user to input amount_1 again if invalid input has been made on amount_2
    try: #test below for errors
        amount_2 = int(input("Enter second amount in cents - ")) #define variable and equal to user input. Use int() function to convert standard string input to a integer. This will be later needed for sum operation
        break #exit loop if input valid
    except ValueError: #do the below if input is invalid
        print("Your input is invalid, please enter a whole number in cents - ") #promt the user to re-input as previous input was invalid

sum = (amount_1 + amount_2)/100 #convert cents to euro

print("The sum of these (in Euro) is ","€",sum,sep="") #print result with euro sign added & remove standard seperators before and after values


'''
Resources:
The following resources were used in completing this task:
1. How to check that the input is an integer, Stack Overflow - https://stackoverflow.com/questions/5424716/how-can-i-check-if-string-input-is-a-number
2. Error handling try and except, W3schools - https://www.w3schools.com/python/python_try_except.asp
3. How a while loop works - previous college coding experience
4. How to remove standard seperators before and after sum value - https://docs.python.org/3/library/functions.html#print

'''