import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1,2,2)

pts = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
], dtype=float)

edges = np.array([
    (0, 1),(0, 3),(1, 2), (3, 2), #bottom
    (4, 5), (4, 7), (5, 6), (7, 6), #top
    (0, 4), (1, 5), (2, 6), (3, 7) # verticle
])

def drawCube(ax, points):
    for e in edges:
        p1 = points[e[0]]
        p2 = points[e[1]]

        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color ='red')

def Oblique(ax, points):
    L = 0.5
    alpha = np.radians(30)
    p2d = []
    for p in points:
        x, y, z = p[0], p[1], p[2]
        u = x + L*z*np.sin(alpha)
        v = y + L*z*np.cos(alpha)
        p2d.append((u,v))
    
    for e in edges:
        p1 = p2d[e[0]]
        p2 = p2d[e[1]]

        ax.plot([p1[0], p2[0]],[p1[1], p2[1]])


def main():
    
    drawCube(ax1, pts)

    ax1.set_title("3D View")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_zlabel("Z")

    Oblique(ax2, pts)
    ax2.set_title("Oblique Projection")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")

    plt.show()

main()            
