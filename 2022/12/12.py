import numpy as np


def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


data = []
for line in open(0).read().splitlines():
    data.append(list(line))


def legal_moves(map, pos, goal):
    moves = []
    if pos[0] > 0:
        if np.abs(map[pos[0]-1, pos[1]] - map[pos[0], pos[1]]) < 1:
            moves.append([pos[0]-1, pos[1]])
    if pos[0] < map.shape[0]:
        if np.abs(map[pos[0]+1, pos[1]] - map[pos[0], pos[1]]) < 1:
            moves.append([pos[0]+1, pos[1]])
    if pos[1] > 0:
        if np.abs(map[pos[0], pos[1]-1] - map[pos[0], pos[1]]) < 1:
            moves.append([pos[0], pos[1]-1])
    if pos[1] < map.shape[1]:
        if np.abs(map[pos[0], pos[1]+1] - map[pos[0], pos[1]]) < 1:
            moves.append([pos[0], pos[1]+1])


heightmap = np.zeros((len(data), len(data[0])))
pathstried = np.zeros((len(data), len(data[0])))
for i in range(heightmap.shape[0]):
    for j in range(heightmap.shape[1]):
        heightmap[i, j] = ord(data[i][j])-97
        if heightmap[i, j] == -14:
            heightmap[i, j] = 0
            start = (i, j)
        if heightmap[i, j] == -28:
            heightmap[i, j] = 26
            end = (i, j)

explored = set(start)
paths = []
pos = list(start)
while True:
    break
print(heightmap)

