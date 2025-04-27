# Programming and Scripting Weekly Tasks
# Overview
This repository contains my project work for the Programming and Scripting module, consisting of 8 weekly programming tasks that demonstrate progressive learning and application of Python concepts. Each task is stored in its own folder (Week-01 through Week-08) with appropriate documentation and commenting.

# Repository Structure

### Week-01
helloworld.py       
- Simple "Hello World" program
### Week-02
bank.py             
- Program to add money amounts and format output
### Week-03
accounts.py         
- Account number masking program
### Week-04
collatz.py          
- Implementation of the Collatz conjecture
### Week-05
weekday.py          
- Program to check if today is a weekday
### Week-06
squareroot.py       
- Custom square root function using Newton's method
### Week-07
es.py               
- Program to count letter 'e' in a text file
### Week-08
 plottask.py         
 - Data visualization program
 
 plottask_result.png 
 - Output image of the visualization

# Weekly Tasks Description

## Week 1: Hello World
A simple introduction to Python programming, creating a basic script that prints "Hello World" to the console. This establishes the development environment and confirms Python is working correctly.

## Week 2: Bank
A program that:
- Takes two money amounts (in cents) as input
- Adds the amounts together
- Displays the result in a human-readable format with euro symbol (€)
- Includes input validation to ensure only valid integers are accepted

## Week 3: Account Numbers
A program that masks account numbers for privacy:
- Reads an account number of any length (minimum 4 digits)
- Displays only the last 4 digits, replacing all other digits with 'X'
- Includes validation to ensure the input contains only digits

## Week 4: Collatz Conjecture
An implementation of the Collatz conjecture which:
- Takes a positive integer as input
- If the number is even, divides it by 2
- If the number is odd, multiplies it by 3 and adds 1
- Continues until the value reaches 1
- Displays the entire sequence on a single line

## Week 5: Weekday Checker
A program that determines if the current day is a weekday:
- Uses the datetime module to get the current day
- Outputs different messages for weekdays and weekends

## Week 6: Square Root Calculator
A custom implementation of a square root calculator:
- Creates a function that approximates square roots using Newton's method
- Takes a positive floating-point number as input
- Outputs the approximated square root
- Compares the result with Python's built-in square root function

## Week 7: Letter Counter
A command-line program that:
- Takes a filename as a command-line argument
- Counts the occurrences of the letter 'e' in the text file
- Includes comprehensive error handling (file not found, incorrect file type, etc.)
- Provides helpful feedback to the user when errors occur

## Week 8: Data Visualization
A program that creates a visualization displaying:
- A histogram of 1000 values from a normal distribution (mean=5, std=2)
- A plot of the cubic function h(x)=x³ over the range [0,10]
- Both visualizations on the same set of axes

# Running the Programs
Each program can be run from its respective folder using Python:
- python Week-01/helloworld.py
- python Week-02/bank.py
- etc.

For Week-07's program, provide a text file name as an argument (moby-dict.txt). This file should be in the same directory as the es.py file otherwise code needs to be updated for location of txt file. 

# Development Approach
Each weekly task builds upon knowledge gained in previous weeks, demonstrating progression in Python programming skills. The code is written with clarity and efficiency in mind, with extensive comments explaining the logic and approach taken.

# Research and References
Each task includes documented research sources that were consulted during development. These references demonstrate the research process undertaken to solve each programming challenge and are cited at the end of each program file.

# Author
Hugo van Zyl
