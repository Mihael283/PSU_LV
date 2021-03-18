import numpy 
import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt(open("/home/profesor/PSU_LV/LV2/mtcars.csv","rb"), usecols(1,2,3,4,5,6), delimiter=",", skiprows=1)
matplotlib.pyplot.scatter(data)
plt.show()