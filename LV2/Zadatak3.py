import numpy as np
from matplotlib import pyplot
from matplotlib import pyplot as plt

data = np.loadtxt(open("/home/profesor/PSU_LV/LV2/mtcars.csv","rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
print(data)


pyplot.scatter(data[:,0],data[:,3],c='b',s=data[:,2])


print(min(data[:,0]))
print(max(data[:,0]))
print(sum(data[:,0]))
arr=[]
for i in data[:,1]:
    if i>=6:
        arr.append(i)

print(min(arr))
print(max(arr))
print(sum(arr))
    


plt.show()