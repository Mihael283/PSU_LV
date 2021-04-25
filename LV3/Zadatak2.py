
import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')


plt.figure()

mtcars.groupby(['cyl']).size().plot.bar(y='mpg',stacked=True)
plt.show()


boxplot= mtcars.boxplot(by='cyl', column=['wt'])
plt.show()


ax= mtcars.groupby(['am']).size().plot.bar(y='',color=('Darkblue','Red'), stacked=True)

ax.set(xlabel=' 0-MANUAL 1-AUTOMATIC',ylabel='MPG')
plt.show()
