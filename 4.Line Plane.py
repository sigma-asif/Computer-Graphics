import numpy as np
import matplotlib.pyplot as plt
#2x − y + z = 4.
#line r = (1,2,3) + t(2,-1,1)
# x=1+2t,y=2−t,z=3+t
# draw plane
xx, yy = np.meshgrid(np.linspace(-5, 5, 100),np.linspace(-5, 5, 100))
zz = 4 + yy - 2*xx

#draw line
t = np.linspace(-3, 3, 100)
xl = 1+t
yl = 2 - t
zl = 3 + t

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(xx, yy, zz, alpha=0.4, color ='steelblue')
    ax.plot(xl, yl, zl)
    ax.set_xlabel('X')    
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.legend()

    plt.show()
main()    