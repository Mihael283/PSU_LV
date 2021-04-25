import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')
print(mtcars)

print(mtcars.sort_values('mpg', ascending=True).nsmallest(5, 'mpg'))

print("Koja tri automobila s 8 cilindara imaju najmanju potrošnju? ",mtcars[mtcars.cyl == 8].sort_values('cyl', ascending=True).nlargest(3, 'cyl'))

cyl_cars = mtcars[mtcars.cyl == 6]
print("Kolika je srednja potrošnja automobila sa 6 cilindara? ",cyl_cars['mpg'].mean())

mass_cars=mtcars[(mtcars.wt>=2) & (mtcars.wt<=2.2) & (mtcars.cyl==4)]
print("Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs? ", mass_cars['mpg'].mean())

am_cars=mtcars[mtcars.am==1]
print("Broj automobila sa automatskim mjenjačem:",am_cars['am'].count())

noam_cars=mtcars[mtcars.am==0]
print("Broj automobila bez automatskog mjenjača:",noam_cars['am'].count())

amhp_cars=mtcars[(mtcars.am==1) & (mtcars.hp>100)]
print("Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga? ", amhp_cars['hp'].count())

print("Kolika je masa svakog automobila u kilogramima? ",mtcars.wt * 1000 * 0.45359237)


mtcars.groupby(['cyl','cyl']).size().unstack().plot.bar(stacked=True)
plt.show()
