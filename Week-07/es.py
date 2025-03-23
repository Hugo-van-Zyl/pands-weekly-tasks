'''
Assignment summary:
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

'''
# es.py
# author - Hugo van Zyl

import sys  # Import sys to handle command-line arguments
import os   # Import os to check file properties (e.g., if a file exists)

def count_e(FILENAME): # function to read a file and count how many times the letter 'e' occurs
    
    try: #try the following code and check for errors
        # Check if the file exists before proceeding
        if not os.path.isfile(FILENAME):
            print(f"Error: The file '{FILENAME}' does not exist.")

            # List all files in the current directory    
            print("These are the available files in the current directory: ")   
            current_dirfiles = os.listdir() # use pythin os function
    
            # Print each file name using for loop to iterate through each file and print
            for file in current_dirfiles:
                print(file)

            print("\nNote this script only accepts (.txt) files")

            return 0  # Return 0 as there's no file to process
            

        # Check if the file has a ".txt" extension (only text files are allowed)
        if not FILENAME.endswith(".txt"):
            print("Error: Only text files (.txt) are supported.")  # Print error if file type is invalid
            return 0  # Return 0 since processing can't continue

        # Initialize a counter to keep track of occurrences of 'e'
        e_count = 0

        # Open the file in read mode ('r') and process it line by line
        with open(FILENAME, "r") as f:
            for line in f:  # Iterate over each line in the file
                e_count += line.count('e')  # Count 'e' (I am looking for lower case 'e' letters only. If I was looking for 'E' and 'e' I would have done lower().count('e))

        return e_count  # Return the total count of 'e' found in the file

    except Exception as e:  # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")  # Print the error message
        return 0  # Return 0 to indicate no file to process

# Ensure the script is run with exactly one command-line argument
if len(sys.argv) != 2: # ensures that multiple arguments are not passed in for the filename
    print("Usage format to run this program is: python es.py <filename>")  # Show correct usage if incorrect arguments are given
else:
    FILENAME = sys.argv[-1]  # Get the filename from the command-line argument (last argument in sys.argv)
    result = count_e(FILENAME)  # Call the function to count 'e' occurrences in the file

    # If counting was successful (not 0 due to an error), print the result
    if result != 0:
        print(f"The file '{FILENAME}' contains {result} instances of the lower case letter 'e'")

'''
Resources:
The following resources were used in completing this task:
1. How to get the filename from command line inut - https://stackoverflow.com/questions/7033987/get-a-file-from-cli-input
                                                  - https://docs.python.org/3/library/sys.html
2. How to read in a text file in python - https://www.w3schools.com/python/python_file_open.asp
3. How to return a list of all files in current durectory - https://www.w3schools.com/python/ref_os_listdir.asp

'''