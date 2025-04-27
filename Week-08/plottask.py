'''
Assignment summary:

Write a program called plottask.py that displays:

 - a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
 - and a plot of the function h(x)=x3 in the range 0 to 10, 

on the one set of axes.
Some marks will be given for making the plot look nice (legend etc).

Please put a copy of the image of the plot (.png file) into the repository

'''
# plottask.py
# author - Hugo van Zyl

#Import standard libraries/modules

import numpy as np #import standard library numpy to work with arrays
import matplotlib.pyplot as plt #import standard plotting library

plt.figure(figsize=(13, 8)) #set the size of the figure that I want to ensure everything is clearly displayed

#Use numpy function to create normal distribution values array
normal_distr = np.random.normal(5, 2, 1000) #set mean to 5 and then standard deviation to 2 and last value to number of values

#Create histogram
plt.hist(normal_distr, bins = 20, color='green', edgecolor='black', label='Normal Distribution (Mean=5 & Std Dev=2)') #use standard function to create histogram. Set color and edge color, set nr bins for clearer plot plus state label

#Use numby linspace function for my x values
xvals = np.linspace(0, 10, 50) #(start,stop, nr of samples)

#Use array arithmatic to get cube values
yvals = xvals**3 #create seperate array of x value to the power of 3

plt.plot(xvals, yvals, color='red', linewidth=2, label='$h(x) = x³$') #plot values of x versus y and $ sign converts equation to scientific notation as learned in data science module

plt.title("Normal distribution and exponential function graph")
plt.xlabel("x-value") # set x axis label
plt.ylabel("y-value") # set y axis label
plt.xlim(0,10) # Set the range of x-axis
plt.legend() #display the legend labels on the plot

plt.show() #display all active plots on same figure


'''
Resources:
The following resources were used in completing this task:
1. Function to generate random values with a specified mean and standard deviation - https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html
2. Function to generate a histogram - https://www.w3schools.com/python/matplotlib_histograms.asp
3. Additional parameters that can be set on plt.hist function - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
4. Create evenly spaced numbers over a range - https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
5. Set parameters of plt.plot function - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
6. Set plot labels, limits and legend - learned in other data science module coursework
'''