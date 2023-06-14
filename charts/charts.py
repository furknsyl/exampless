##bar chart
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('populations.csv')

data=[go.Bar(
    x=df['NOS'],
    y=df['POPULATIONS']
)]

layout=go.Layout(

     title='City populations in Turkey'
)

fig=go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar.html')

##pie chart
import matplotlib.pyplot as plt
labels = 'Farm', 'Endustriel', 'Service'
sizes = [7.8, 19.6,72.6]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.set_title("Sectoral distribution of the Turkish economy", fontsize=24)
plt.savefig('pies.png', dpi=300, bbox_inches='tight')
plt.show()

##tems chart
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/andrzejmp/some_codes/main/python/temperatures/data.csv')

highs = df["TMAX"].tolist()
lows = df["TMIN"].tolist()


for i in range(len(highs)):
    highs[i] = (highs[i] - 32) / 1.8
    lows[i] = (lows[i] - 32) / 1.8


import matplotlib.pyplot as plt
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')
ax.plot(lows, c='blue')

ax.set_title("Maximum and minimum temperatures in Death Valley, 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (C)", fontsize=16)
plt.savefig('temps.png', dpi=300, bbox_inches='tight')
plt.show()
##tourism chart

import matplotlib.pyplot as plt
import numpy as np

species = ("2018", "2019", "2020")
rankings = {
    'Turkey': (45, 51, 60),
    'Spain': (60,70, 80),
    'France': (70, 80, 96),
}

x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in rankings.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel('Million')
ax.set_title('Tourism Ranking')
ax.set_xticks(x + width, species)
ax.set_ylim(0, 250)
plt.savefig('rankings.png')
plt.show()
