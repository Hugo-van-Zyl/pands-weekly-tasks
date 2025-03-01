'''
Assignment summary:
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

You will need to search the web to find how you work out what day it is.
'''
# weekday.py
# author - Hugo van Zyl
import datetime # import datetime module which provides classes for working with dates and times

today = datetime.date.today().weekday()  #I am using the class datetime.date as I am only looking for day and not concerned about getting the time. 
#.today() returns the current date (today)
#.weekday() gets what day it is today and returns this as an integer from 0 (Monday) to 6 (Saturday)

weekday = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4} # create dictionary of weekdays and their corresponding value next to the key
weekend = {"Saturday":5, "Sunday":6} # create dictionary of weekend and their corresponding value next to the key

for x in weekday.values(): # loop through all of the values in the weekday dictionary
    if today == x: # if today's number value matches the equavalent number representation of days, do the following
        print("Yes, unfortunately today is a weekday.") # if true, print this message
        break # exit loop if number found
         # no else statement as the today variable will always be between 0 and 6

for y in weekend.values(): # loop through all of the values in the weekday dictionary
    if today == y: # if today's number value matches the equavalent number representation of days, do the following
        print("It is the weekend, yay!") # if true, print this message
        break # exit loop if number found
        # no else statement as the today variable will always be between 0 and 6

#print(weekday.values()) I used this to check what the .values() returned and confirmed it is the nr values in each directory linked with the day name

'''
Resources:
The following resources were used in completing this task:
1. Find out what day is today - https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
2. Python datetime - https://docs.python.org/3/library/datetime.html
3. How to loop through a dictionary & access dictionary values - https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp
'''