import urllib.request, json
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/json?postaja=160&polutant=5&tipPodatka=4&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'

airQualityHR = urllib.request.urlopen(url).read()
data = json.loads(airQualityHR)

df = pd.DataFrame(data,columns=('vrijednost','vrijeme'))
df.reset_index(drop=True,inplace=True)
df.vrijeme = pd.to_datetime(df.vrijeme,utc=True,unit='ms')
print("Datum i iznos najveće koncentracije lebdećih čestica u 2017 godini: \n",df.iloc[df.vrijednost.argsort()[-3:]])
df['month']= pd.DatetimeIndex(df.vrijeme).month

zima = df[df['month']==1]
ljeto = df[df['month']==7]


boxplot= df.boxplot(by='vrijednost',column=['month'])
plt.show()
