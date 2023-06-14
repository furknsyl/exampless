##pie chart
import matplotlib.pyplot as plt
labels = 'Farm', 'Endustriel', 'Service'
sizes = [7.8, 19.6,72.6]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.set_title("Sectoral distribution of the Turkish economy", fontsize=24)
plt.savefig('pies.png', dpi=300, bbox_inches='tight')
plt.show()