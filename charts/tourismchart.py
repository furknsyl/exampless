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