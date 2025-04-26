import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Create a RandomWalk instance
rw = RandomWalk(10000)
rw.fill_walk()

# Plotting
plt.style.use('classic') 
figure, graph = plt.subplots(figsize=(15, 9)) 

# Scatter all points
graph.scatter(
    rw.x_values, rw.y_values, 
    s=15, c=rw.y_values, cmap=plt.cm.winter, edgecolors='none'
)

# Highlight start point (green)
graph.scatter(0, 0, s=50, color='green', edgecolors='none')

# Highlight end point (red)
graph.scatter(rw.x_values[-1], rw.y_values[-1], s=50, color='red', edgecolors='none')

# Remove axes
graph.get_xaxis().set_visible(False)
graph.get_yaxis().set_visible(False)

plt.show()
