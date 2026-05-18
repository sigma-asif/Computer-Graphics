import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(1,2, 1, projection='3d')
ax2 = fig.add_subplot(1,2,2)

pts = np.array([
    [0, 0, 0], [1, 0, 0], [1,1,0], [0,1, 0],[0, 0, 1], [1, 0, 1], [1,1,1], [0,1, 1]
])
edges = np.array([
    # bottom
    (0,1), (0, 3), (1,2),(2,3),
    #top
    (4, 5),(4,7), (5, 6),(6, 7),
    #verticles
    (0,4),(1, 5),(2, 6),(3,7)
])

def drawCube(ax, points):
    for e in edges:
        p1 = points[e[0]]
        p2 = points[e[1]]

        ax.plot([p1[0],p2[0]], [p1[1], p2[1]], [p1[2], p2[2]])


def cameraProj(ax,points):  
    cx, cy = 500, 400
    fx, fy = 800, 800
    C = np.array([0.5, 0.5, -5])
    '''
    R = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    '''
    R = np.eye(3)
    
    
    Pc = (R@(points-C).T).T
    p2d =[]
    for x, y, z in Pc:
        if z <= 0:
            z = 0.001

        u = (x*fx)/(z) + cx
        v = (y*fy)/(z) + cy

        p2d.append((u, v))

    for e in edges:
        p1 = p2d[e[0]]
        p2 = p2d[e[1]]
        ax.plot([p1[0], p2[0]],[p1[1],p2[1]])    




def main():
    drawCube(ax1, pts)
    ax1.set_title('3d cube')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')

    cameraProj(ax2,pts)
    ax2.set_title('Camera Projected Cube')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')

    plt.show()

main()

