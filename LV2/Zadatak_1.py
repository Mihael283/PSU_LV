import numpy as np
import matplotlib.pyplot as plt
mu = 3
sigma = 2
v = np.random.normal(mu,sigma,10000)
plt.hist(v, bins=50, normed=1)
plt.show()
