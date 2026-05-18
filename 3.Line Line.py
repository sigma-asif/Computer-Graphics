import numpy as np
import matplotlib.pyplot as plt
# L1: a1x + b1y + c1 = 0
a1, b1, c1 = 2, 3, -6      # 2x + 3y- 6 = 0

# L2: a2x + b2y + c2 = 0
a2, b2, c2 = 1, -1, -1     # x - y -1 = 0

def intersect():
    D = a1*b2 - a2*b1
    Dx = b1*c2 - b2*c1
    Dy = -a1*c2 +c1*a2

    x = Dx/D
    y = Dy/D

    return x, y



def main():
    x,y = intersect()
    X = np.linspace(-2, 5, 100)
    Y1 = (6 - 2*X)/3
    Y2 = (X-1)

    plt.plot(X, Y1, label ='L1')
    plt.plot(X, Y2, label = 'L2')
    plt.scatter(x, y, color ='red', label ='X')
    plt.legend()
    plt.grid()
    plt.show()


main()    