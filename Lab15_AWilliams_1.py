""" 
Author: Ambrea Williams
Date: 04/24/2025
Project: Lab 15 / Graphing Data
Description: This program will take a particular math formula and plot it on a graph.
"""
import matplotlib.pyplot as plt
#import numpy as np

ind_var = range (1, 6) # Independent variable
dep_var = [x * x for x in ind_var] # Dependent variable

"""Plotting the data"""
figure, graph = plt.subplots() # Create a figure and axis
graph.plot(ind_var, dep_var, linewidth=3, color='blue') # Plot the data
graph. set_title('')

plt.show()


