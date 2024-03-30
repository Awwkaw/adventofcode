from collections import deque
import sys
sys.setrecursionlimit(1400)
testdirs = [
        [1, 0, 0],
        [-1, 0, 0],
        [0, -1, 0],
        [0, 1, 0],
        [0, 0, -1],
        [0, 0, 1],
        ]


def test_spot(coord):
    surface = 0
    for testdir in testdirs:
        testcoord = tuple([x0 + x1 for x0, x1 in zip(coord, testdir)])
        if testcoord not in lava:
            surface += 1

    return surface


def test_region(queue: deque, visited: set):
    while queue:
        coord = queue.popleft()
        if coord in visited:
            continue
        visited.add(coord)
        if coord in lava or any([
                x < minval or x > maxval for x, minval, maxval
                in zip(coord, min_coord, max_coord)]):
            continue
        for testdir in testdirs:
            testcoord = tuple([x0 + x1 for x0, x1 in zip(coord, testdir)])
            if any([
                    x < minval or x > maxval for x, minval, maxval
                    in zip(testcoord, min_coord, max_coord)]):
                return None
            if testcoord not in lava \
                    and testcoord not in visited\
                    and testcoord not in queue:
                queue.append(testcoord)
        return test_region(queue, visited)
    return visited


lava = set()
min_coord = (20, 20, 20)
max_coord = (0, 0, 0)

for line in open(0).read().splitlines():
    coord = tuple([c for c in map(int, line.split(','))])
    lava.add(coord)
    min_coord = tuple([min(x0, x1) for x0, x1 in zip(coord, min_coord)])
    max_coord = tuple([max(x0, x1) for x0, x1 in zip(coord, max_coord)])


surface = 0
for coord in lava:
    surface += test_spot(coord)
print(surface)

for x in range(min_coord[0], max_coord[0]):
    for y in range(min_coord[1], max_coord[1]):
        for z in range(min_coord[2], max_coord[2]):
            if test_spot((x, y, z)) == 0:
                lava.add((x, y, z))

surface = 0
for coord in lava:
    surface += test_spot(coord)
print(surface)


to_check = set()
for coord in lava:
    for testdir in testdirs:
        testcoord = tuple([x0 + x1 for x0, x1 in zip(coord, testdir)])
        if testcoord not in lava and all([
                x >= minval and x <= maxval
                for x, minval, maxval in
                zip(testcoord, min_coord, max_coord)]):
            to_check.add(testcoord)


for coord in to_check:
    res = test_region(deque([coord]), set())
    if res is not None:
        lava |= res

surface = 0
for coord in lava:
    surface += test_spot(coord)
print(surface)
