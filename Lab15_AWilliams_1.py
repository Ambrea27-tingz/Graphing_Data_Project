""" 
Author: Ambrea Williams
Date: 04/24/2025
Project: Graphing Data
Unit 14: Lab 15, Opt 1
Description: This program will take a particular math formula and plot it on a graph.
"""
import matplotlib.pyplot as plt
#import numpy as np

"""Our data"""
ind_var = range (1, 6) # Independent variable
dep_var = [x * x for x in ind_var] # Dependent variable

"""Plotting the data"""
figure, graph = plt.subplots() # Create a figure and axis
graph.plot(ind_var, dep_var, linewidth=3, color='blue') # Plot the data
graph.set_title('Graph of y = x^2')

plt.show()


