import numpy as np


def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


data = []
for line in open(0).read().splitlines():
    data.append(list(line))


def find_legal_moves(map, pos, goal):
    moves = []
    if pos[0] > 0:
        if (map[pos[0]-1, pos[1]] - map[pos[0], pos[1]]) <= 1:
            moves.append([pos[0]-1, pos[1]])
    if pos[0] < map.shape[0]-1:
        if (map[pos[0]+1, pos[1]] - map[pos[0], pos[1]]) <= 1:
            moves.append([pos[0]+1, pos[1]])
    if pos[1] > 0:
        if (map[pos[0], pos[1]-1] - map[pos[0], pos[1]]) <= 1:
            moves.append([pos[0], pos[1]-1])
    if pos[1] < map.shape[1]-1:
        if (map[pos[0], pos[1]+1] - map[pos[0], pos[1]]) <= 1:
            moves.append([pos[0], pos[1]+1])
    return moves


heightmap = np.zeros((len(data), len(data[0])))
for i in range(heightmap.shape[0]):
    for j in range(heightmap.shape[1]):
        heightmap[i, j] = ord(data[i][j])-97
        if heightmap[i, j] == -14:
            heightmap[i, j] = 0
            start = (i, j)
        if heightmap[i, j] == -28:
            heightmap[i, j] = 26
            end = (i, j)

score_map = np.inf*np.ones(heightmap.shape, np.int)
for step in range(len(heightmap.flatten())):
    if step == 0:
        score_map[start[0], start[1]] = 0

    to_check = score_map == step
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            if not to_check[i, j]:
                continue
            legal_moves = find_legal_moves(heightmap, (i, j), end)
            for legal_move in legal_moves:
                if not score_map[legal_move[0], legal_move[1]] > step+1:
                    continue
                score_map[legal_move[0], legal_move[1]] = step+1

    if score_map[end[0], end[1]] != np.inf:
        break

print(int(score_map[end[0], end[1]]))

scores = [int(score_map[end[0], end[1]])]
start_points = heightmap == 0
tested = np.zeros(heightmap.shape)
previous_step = np.inf * np.ones(heightmap.shape)

for x in range(heightmap.shape[0]):
    for y in range(heightmap.shape[1]):
        if not start_points[x, y]:
            continue
        done = False
        score_map = np.inf*np.ones(heightmap.shape, np.int)
        for step in range(len(heightmap.flatten())):
            if step == 0:
                score_map[x, y] = 0
            if step >= min(scores):
                break
            to_check = score_map == step
            for i in range(heightmap.shape[0]):
                for j in range(heightmap.shape[1]):
                    if not to_check[i, j] or\
                            score_map[i, j] > 1+previous_step[i, j] or \
                            done:
                        continue
                    legal_moves = find_legal_moves(heightmap, (i, j), end)
                    for legal_move in legal_moves:
                        if not score_map[
                                legal_move[0],
                                legal_move[1]
                                ] > step+1 or\
                                tested[
                                legal_move[0],
                                legal_move[1]
                                ] == 1:
                            continue
                        score_map[legal_move[0], legal_move[1]] = step+1
                        if end[0] == legal_move[0] and\
                                end[1] == legal_move[1]:
                            done = True
                            scores.append(step + 1)
                            previous_step = np.min([previous_step, score_map],
                                                   axis=0)
        tested[x, y] = 1


for x in range(heightmap.shape[0]):
    for y in range(heightmap.shape[1]):
        if not start_points[x, y]:
            continue
        done = False
        score_map = np.inf*np.ones(heightmap.shape, np.int)
        for step in range(len(heightmap.flatten())):
            if step == 0:
                score_map[x, y] = 0
            if step >= min(scores):
                break
            to_check = score_map == step
            for i in range(heightmap.shape[0]):
                for j in range(heightmap.shape[1]):
                    if not to_check[i, j] or\
                            score_map[i, j] > 1+previous_step[i, j] or \
                            done:
                        continue
                    legal_moves = find_legal_moves(heightmap, (i, j), end)
                    for legal_move in legal_moves:
                        if not score_map[
                                legal_move[0],
                                legal_move[1]
                                ] > step+1 or\
                                tested[
                                legal_move[0],
                                legal_move[1]
                                ] == 1:
                            continue
                        score_map[legal_move[0], legal_move[1]] = step+1
                        if end[0] == legal_move[0] and\
                                end[1] == legal_move[1]:
                            done = True
                            scores.append(step + 1)
                            previous_step = np.min(
                                    [previous_step, score_map],
                                    axis=0
                                    )
        tested[x, y] = 1

print(min(scores))
print(scores)
