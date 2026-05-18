import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(1,2,1, projection='3d')
ax2 = fig.add_subplot(1,2,2, projection='3d')

state ={'x':0.0, 'y':0.0, 'z':0.0}
pts = np.array([
    [0,0,0],[1,0,0],[1,1,0],[0,1,0],
    [0,0,1],[1,0,1],[1,1,1],[0,1,1] 
], dtype=float)

edges = [
    # Bottom face (z=0)
    (0, 1), (1, 2), (2, 3), (3, 0),
    # Top face (z=1)
    (4, 5), (5, 6), (6, 7), (7, 4),
    # Vertical pillars (connecting bottom to top)
    (0, 4), (1, 5), (2, 6), (3, 7)
]
def drawCube(ax, points, edges):
    ax.cla()
    for e in edges:
        p1 = points[e[0]]
        p2 = points[e[1]]

        ax.plot([p1[0], p2[0]],[p1[1],p2[1]],[p1[2], p2[2]], color ='red')   

def rotate(points):
    center = np.array([0.5, 0.5, 0.5])
    tx, ty, tz = np.radians(state['x']), np.radians(state['y']), np.radians(state['z'])
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(tx), -np.sin(tx)],
        [0, np.sin(tx), np.cos(tx)]
    ], dtype=float)        
    Ry = np.array([
        [np.cos(ty), 0, np.sin(ty)],
        [0, 1, 0],
        [-np.sin(ty), 0, np.cos(ty)]
    ], dtype=float)  

    Rz = np.array([
        [np.cos(tz), -np.sin(tz), 0],
        [np.sin(tz), np.cos(tz), 0],
        [0, 0, 1]
    ], dtype=float)  

    R = Rz@Ry@Rx
    shifted_pts = points - center
    rotated_pts = (R@shifted_pts.T).T
    fpts = rotated_pts + center
    return fpts

def redraw():
    drawCube(ax1, pts, edges)
    ax1.set_title('Cube 3d')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')

    drawCube(ax2, rotate(pts), edges)
    ax2.set_title('Rotated Cube')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.text2D(0.05,0.95, f"X:{state['x']%360:.0f}° Y:{state['y']%360:.0f}° Z:{state['z']%360:.0f}°",transform=ax2.transAxes, color='black', fontsize=9)
    fig.canvas.draw_idle()


def on_key(event):
    if event.key == '+': state['x']+= 10
    elif event.key == '-': state['x']-= 10
    elif event.key == 'up': state['y']+= 10
    elif event.key == 'down': state['y']-= 10
    elif event.key == 'left': state['z']+= 10
    elif event.key == 'right': state['z']-= 10
    else:return

    redraw()


def main():
    
    ax2.disable_mouse_rotation()
    fig.canvas.mpl_connect('key_press_event', on_key)
    redraw()
    plt.show()


main()    