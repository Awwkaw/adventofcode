import numpy as np


def dist(
        h: list,
        t: list
        ) -> float:
    return np.sqrt((h[0]-t[0])**2 + (h[1]-t[1])**2)


def move_leader(
        h: list,
        dir: str
        ) -> list:
    if 'U' in dir:
        h[1] += 1
    elif 'D' in dir:
        h[1] -= 1
    elif 'L' in dir:
        h[0] -= 1
    elif 'R' in dir:
        h[0] += 1
    return h


def move_follower(
        h: list,
        t: list
        ) -> tuple[list, bool]:

    did_move = False

    if h[0] > t[0] + 1:
        t[0] = h[0] - 1
        t[1] += np.sign(h[1]-t[1])
        did_move = True
    elif h[0] < t[0] - 1:
        t[0] = h[0] + 1
        t[1] += np.sign(h[1]-t[1])
        did_move = True
    elif h[1] > t[1] + 1:
        t[1] = h[1] - 1
        t[0] += np.sign(h[0]-t[0])
        did_move = True
    elif h[1] < t[1] - 1:
        t[1] = h[1] + 1
        t[0] += np.sign(h[0]-t[0])
        did_move = True
    return t, did_move


rope_length = 11
# h = [0, 0]
t = [[0, 0] for s in range(rope_length)]
t1 = 0
t2 = 1

coord = 'i0j0'
visited = [[coord] for s in range(rope_length)]

while True:
    try:
        i = input()
    except Exception:
        break

    dir, n = i.split()
    did_move = False
    for i in range(int(n)):
        t[0] = move_leader(t[0], dir)
        for s in range(1, rope_length):
            t[s], did_move = move_follower(t[s-1], t[s])

            if did_move:
                coord = f'i{t[s][0]}j{t[s][1]}'
                if coord not in visited[s]:
                    visited[s].append(coord)
                    if s == 1:
                        t1 += 1
                    if s == 9:
                        t2 += 1
                continue
            break


print(t1)
print(t2)
