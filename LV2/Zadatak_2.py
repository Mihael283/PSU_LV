
import numpy 
import numpy as np
from matplotlib import pyplot as plt


arr=[]
# Pick a seed for the random number generator
np.random.seed(101)
for x in range(100):
    x=np.random.randint(1, 7)
    arr.append(x)

mat = numpy.array(arr)
print(mat)
 
   
plt.hist(mat,bins=(6))
plt.ylim(ymin=0, ymax = 100)
plt.title("histogram") 
plt.show()