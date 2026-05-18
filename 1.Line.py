import numpy as np
import matplotlib.pyplot as plt
# L1: a1x + b1y + c1 = 0
a, b, c = 1, 1, -4      # x + y - 4 = 0

p1 = [-c/a, 0]
p2 = [0, -c/b]

plt.plot(p1, p2, color ='red', label="L1")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line")
plt.grid()
plt.legend()      # add this
plt.show()