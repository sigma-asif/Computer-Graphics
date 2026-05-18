import numpy as np
import matplotlib.pyplot as plt

A = np.array([0, 0, 1])
B = np.array([2, 0, 3])
C = np.array([1, 2, 2])

normal = np.cross(B - A, C - A)
a, b, c = normal
d = np.dot(normal, A)

xx, yy = np.meshgrid(np.linspace(-1, 3, 20), np.linspace(-1, 3, 20))
zz = (d - a * xx - b * yy) / c

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(xx, yy, zz, alpha=0.4, color='steelblue')
ax.scatter(*np.array([A, B, C]).T, color='red', s=60)

for p, name in zip([A, B, C], ['A', 'B', 'C']):
    ax.text(*p, name, fontsize=11)


ax.set_xlabel('X')    
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()