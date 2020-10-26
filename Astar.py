import math
from operator import attrgetter
import matplotlib.pyplot as plt
import cv2
import numpy as np



def calc_f(x, y, goalx, goaly):
    return math.hypot(x - goalx, y - goaly)

class Node:
    def __init__(self, x, y, g):
        self.x = x
        self.y = y
        self.f = calc_f(self.x, self.y, gx, gy) #sqrt(x*x + y*y) 欧几里得
        self.g = g
        self.h = self.f + self.g
        self.pathx = []
        self.pathy = []

    def __add__(self, other):
        return Node(self.x + other[0], self.y + other[1], self.g + w)

    def __repr__(self):
        return str(self.x) + "-" + str(self.y) + "-" + str(self.h)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

def on_EVENT_LBUTTONDOWN(event, x, y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        a.append(x)
        b.append(y)
        cv2.circle(img1, (x, y), 1, (0, 0, 255), thickness=-1)
        cv2.putText(img1, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img1)




w = 1
# steps = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
# steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]
steps = [(0, -2), (2, 0), (0, 2), (-2, 0)]
# steps = [(0, -3), (3, 0), (0, 3), (-3, 0)]
# steps = [(0, -2), (2, -2), (2, 0), (2, 2), (0, 2), (-2, 2), (-2, 0), (-2, -2)]

filename = "maze1.png"
img = cv2.imread(filename)[:, :,0]

# img = cv2.resize(img, (100, 25), interpolation=cv2.INTER_AREA)

borders = img.shape

img = cv2.flip(img, 0)

np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf) # 这个参数填的是横向多宽


img1 = cv2.imread(filename)
img1 = cv2.flip(img1, 0)
a =[]
b = []
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img1)
cv2.waitKey(0)

#起点
sx,sy = a[0],b[0]

#终点
gx,gy = a[1],b[1]


print(sx,sy)
print(gx,gy)

ox = list()
oy = list()

#img.shape (519, 552)
#ox,oy是不能走的地方
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i, j] < 100:
        # if img[i, j] != 255:	
            ox.append(j)
            oy.append(i)

current_node = Node(sx, sy, 0)

queue = [current_node]
discarded = list()

pathx = list()
pathy = list()

while not len(queue) == 0:
    current_node = min(queue, key=attrgetter('h'))
    if calc_f(current_node.x, current_node.y, gx, gy) < 2:
        pathx = current_node.pathx
        pathy = current_node.pathy
        break
    current_index = queue.index(min(queue, key=attrgetter('h')))
    # print(current_node)
    for i in steps:
        neighbor = current_node + i
        if not((neighbor.x, neighbor.y) in zip(ox, oy)): #如果可以走通
            if neighbor not in discarded:
                if (0 <= neighbor.x <= borders[1]) and (0 <= neighbor.y <= borders[0]):
                    if neighbor not in queue:
                        neighbor.pathx = current_node.pathx + [neighbor.x]
                        neighbor.pathy = current_node.pathy + [neighbor.y]
                        queue.append(neighbor)

    del current_node.pathy, current_node.pathx
    discarded.append(current_node)
    del queue[current_index]
    # print(queue)

plt.plot(gx, gy, "xb")
plt.plot(sx, sy, "xc")
plt.plot(ox, oy, ".k")
plt.plot(pathx, pathy, "-r")
plt.grid(True)
plt.axis("equal")

plt.show()








