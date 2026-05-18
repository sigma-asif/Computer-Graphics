import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

pts = np.array([
    [0,0,0],[1,0,0],[1,1,0],[0,1,0],
    [0,0,1],[1,0,1],[1,1,1],[0,1,1]
], dtype=float)

edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]
def drawCube(ax, points):
    for e in edges:
        p1 = points[e[0]]
        p2 = points[e[1]]

        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color ='red')

def transform(ax, points):
    tx, ty, tz = 0.5, 0.5, 0.5         # translation amounts
    sx, sy, sz = 2,2,4
    angle = np.radians(45)
    T1 = np.array([
        [1, 0, 0, -tx],
        [0, 1, 0, -ty],
        [0, 0, 1, -tz],
        [0, 0, 0, 1]
    ])
    S = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    Rx = np.array([
        [1,           0,            0, 0],
        [0, np.cos(angle), -np.sin(angle), 0],
        [0, np.sin(angle),  np.cos(angle), 0],
        [0,           0,            0, 1]
    ])
    T2 = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
    # add 4th column of 1s to pts → homogeneous coordinates
    #pts_h = np.hstack([pts, np.ones((len(pts), 1))])  # (8,4)
    hpts = np.hstack([pts, np.ones((len(pts), 1))])
    
    M = T2@Rx@S@T1
    npts = (M @ hpts.T).T

    for e in edges:
        p1 = npts[e[0]]
        p2 = npts[e[1]]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color ='red')



def main():
    drawCube(ax1, pts)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('Cube')

    transform(ax2, pts)
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title('Rotated Cube')
    plt.show()

main()    