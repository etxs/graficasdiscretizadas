import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

fig, ax = plt.subplots()

# Elipse
ellipse = Ellipse((5, 5), 4, 2, color='blue', fill=False)
ax.add_patch(ellipse)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.grid(True)
plt.show()