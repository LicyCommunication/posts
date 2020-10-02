# Simulate a Poisson point process on a triangle.
# Author: H. Paul Keeler, 2018.
# Website: hpaulkeeler.com
# Repository: github.com/hpaulkeeler/posts

import numpy as np;  # NumPy package for arrays, random number generation, etc
import matplotlib.pyplot as plt  # for plotting

plt.close('all');  # close all figures

# Simulation window parameters -- points A,B,C of a triangle
xA = 0;
xB = 1;
xC = 1;  # x values of three points
yA = 0;
yB = 0;
yC = 1;  # y values of three points

# Point process parameters
lambda0 = 100;  # intensity (ie mean density) of the Poisson process

# calculate sides of triangle
a = np.sqrt((xA - xB) ** 2 + (yA - yB) ** 2);
b = np.sqrt((xB - xC) ** 2 + (yB - yC) ** 2);
c = np.sqrt((xC - xA) ** 2 + (yC - yA) ** 2);
s = (a + b + c) / 2;  # calculate semi-perimeter

# Use Herron's formula  to calculate the area of triangle
areaTotal=(1/4)*np.sqrt( (a+(b+c))*(c-(a-b))*(c+(a-b))*(a+(b-c))); 

# Simulate a Poisson point process
numbPoints = np.random.poisson(lambda0 * areaTotal);  # Poisson number of points
U = np.random.uniform(0, 1, numbPoints);  # uniform random variables
V = np.random.uniform(0, 1, numbPoints);  # uniform random variables

#places points uniformly on triangle
xx = np.sqrt(U) * xA + np.sqrt(U) * (1 - V) * xB + np.sqrt(U) * V * xC;  # x coordinates of points
yy = np.sqrt(U) * yA + np.sqrt(U) * (1 - V) * yB + np.sqrt(U) * V * yC;  # y coordinates of points

# Plotting
plt.scatter(xx, yy, edgecolor='b', facecolor='none', alpha=0.5);
plt.xlabel('x');
plt.ylabel('y');
plt.show();