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
ind_var = range (1, 10_001) # Independent variable
dep_var = [x * x for x in ind_var] # Dependent variable
plt.style.use('dark_background') # Set the style of the graph

"""Plotting the data"""
figure, graph = plt.subplots() # Create a figure and axis
graph.scatter(ind_var, dep_var, s=10, c=dep_var, cmap=plt.cm.Purples) # Plot the data
graph.set_title('Squared Numbers', fontsize=24)
graph.set_xlabel('Value', fontsize=14) # Set the x-axis label
graph.set_ylabel('Square Values', fontsize=14) # Set the y-axis label
graph.tick_params(labelsize=14, color='red')
graph.axis((1,10000, 1, 100_000_000))
graph.ticklabel_format(axis='y' , style='plain')
#plt.show()
plt.savefig('simple_squares_graph.png', bbox_inches='tight',pad_inches=0.5) # Save the figure




