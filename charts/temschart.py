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