
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')


plt.figure()

mtcars.groupby(['cyl']).size().plot.bar(y='mpg',stacked=True)
plt.show()