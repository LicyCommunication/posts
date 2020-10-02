# Simulate a Poisson point process on a rectangle
# Then thin the Poisson point process according to a (spatially *independent*)
# p-thinning
# Author: H. Paul Keeler, 2019.
# Website: hpaulkeeler.com
# Repository: github.com/hpaulkeeler/posts

import numpy as np;  # NumPy package for arrays, random number generation, etc
import matplotlib.pyplot as plt  # For plotting

plt.close('all');  # close all figures

# Simulation window parameters
xMin = -1;
xMax = 1;
yMin = -1;
yMax = 1;
xDelta = xMax - xMin;
yDelta = yMax - yMin;  # rectangle dimensions
areaTotal = xDelta * yDelta;

# Point process parameters
lambda0 = 100;  # intensity (ie mean density) of the Poisson process

# Thinning probability
p = 0.25;

# Simulate a Poisson point process
numbPoints = np.random.poisson(lambda0 * areaTotal);  # Poisson number of points
xx = xDelta * np.random.uniform(0, 1, numbPoints) + xMin;  # x coordinates of Poisson points
yy = yDelta * np.random.uniform(0, 1, numbPoints) + yMin;  # y coordinates of Poisson points

# Generate Bernoulli variables (ie coin flips) for thinning
booleThinned = np.random.uniform(0, 1, numbPoints) < p;  # points to be thinned
booleRetained = ~booleThinned;  # points to be retained

# x/y locations of thinned points
xxThinned = xx[booleThinned];
yyThinned = yy[booleThinned];
# x/y locations of retained points
xxRetained = xx[booleRetained];
yyRetained = yy[booleRetained];

# Plotting
plt.scatter(xxRetained, yyRetained, edgecolor='b', facecolor='none', alpha=0.5);
plt.scatter(xxThinned, yyThinned, edgecolor='r', facecolor='none', alpha=0.5);
plt.xlabel('x');
plt.ylabel('y');
plt.show();
