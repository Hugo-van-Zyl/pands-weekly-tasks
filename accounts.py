'''
Assignment summary:
Write a python program called accounts.py that reads in a 10 character account number 
and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

Extra:
Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

'''
# accounts.py
# author - Hugo van Zyl

#The below program will read in an account number of any lenght (minimum lenght is 1 digit) and display only the last 4 digits of the account number.
#I am assuming a valid account number is anything with at least 1 character/number

while True: #use while loop to iterate through input until the user has inputted a valid account number
        account_nr = input("Please enter a 1 or more digit account number - ") #define variable and equal to user input. Use int() function to convert standard string input to a integer. 
        account_nr_length = len(account_nr)
        if (account_nr_length>0): #if this condition is met, run the below code. 
            #Note if I wanted only 10 digit account numbers, I would have had account_nr_length == 10
            break #exit loop
        else: #if condition above is not met, run below code
            print("Error - your input was invalid") #display error message to the user


print("The last 4 digits of your account number is - ","X"*(len(account_nr)-4),account_nr[-4:], sep="") 
#sep="" removes space between X and last 4 digits. 
#"X"*(len(account_nr)-4) - prints the nr of X's equal to the account number lenght less the last 4 digits. 
# account_nr[-4:] - uses negative indexing to start at the last 4 numbers from the input and displays everything from there to the end

'''
Resources:
The following resources were used in completing this task:
1. Slicing strings for negative indexing, W3 Schools - https://www.w3schools.com/python/python_strings_slicing.asp
2. Using an If statement - previous college coding experience
3. Using a while loop - previous college coding experience
4. Getting the lenght of a string, W3 Schools - https://www.w3schools.com/python/gloss_python_string_length.asp
5. How to replace first few numbers in string with "X" (i.e. multiply X by lenght number less 4 - ChatGPT

'''