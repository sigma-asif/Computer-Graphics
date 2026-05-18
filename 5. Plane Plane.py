import numpy as np
import matplotlib.pyplot as plt

#x + 2y + 2z = 5 and 2x + y + 2z = 6.
xp1 , yp1 = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)) 
zp1 = (5 - 2*yp1 - xp1)/2

xp2 , yp2 = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)) 
zp2 = (6 - 2*xp2 - yp2)/2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xp1,yp1,zp1, alpha = 0.4, color ='steelblue')
ax.plot(xp2,yp2,zp2, alpha = 0.4, color ='orange')
plt.legend()
plt.show()
