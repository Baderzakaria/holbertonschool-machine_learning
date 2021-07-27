#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [68, 80]
cov = [[15, 8], [8, 15]]
np.random.seed(10)
x, y = np.random.multivariate_normal(mean, cov, 200).T
y += 180

plt.scatter(x, y, c='m')
plt.xlabel("Height (in)")
plt.ylabel("Weight (lbs)")
plt.title("Men's Height vs Weight")
plt.show()
