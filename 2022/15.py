data = open(0).read().splitlines()
beacons = []
sensors = []
on_line = set()

for line in data:
    s, b = line.split(':')
    s = [int(i.split('=')[-1]) for i in s.split(',')]
    b = [int(i.split('=')[-1]) for i in b.split(',')]
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
    sensors.append([s] + [dist])

test_line = 10
# test_line = 2000000

for sensor in sensors:
    if abs(sensor[0][1] - test_line) <= sensor[1]:
        r = sensor[1] - abs(sensor[0][1] - test_line)
        for x in range(sensor[0][0]-r, sensor[0][0]+r):
            on_line.add((test_line, x))


print(len(on_line))

ul = 20 # test
ul = 4000000


neighbor = set()
removed = set()
remove_sensors = set()

for i, sensor in enumerate(sensors):
    for k, testsensor in enumerate(sensors):
        if i == k:
            continue
        dist = abs(sensor[0][0] - testsensor[0][0]) +\
            abs(sensor[0][1] - testsensor[0][1])
        if dist < testsensor[1] and testsensor[1] - dist > sensor[1]:
            remove_sensors.add(i)

for idx in list(remove_sensors)[::-1]:
    sensors.pop(idx)

for (coord, dist) in sensors:
    print(dist, flush=True)
    for xc, yc in zip(range(0, dist+1), range(dist, -1, -1)):
        c1 = (coord[0] + xc + 0, coord[1] + yc + 1)
        c2 = (coord[0] + xc + 1, coord[1] - yc + 0)
        c3 = (coord[0] - xc - 1, coord[1] + yc + 0)
        c4 = (coord[0] - xc + 0, coord[1] - yc - 1)
        if c1[0] > 0 and c1[0] < ul+1 and c1[1] > 0 and c1[1] < ul + 1:
            neighbor.add(c1)
        if c2[0] > 0 and c2[0] < ul+1 and c2[1] > 0 and c2[1] < ul + 1:
            neighbor.add(c2)
        if c3[0] > 0 and c3[0] < ul+1 and c3[1] > 0 and c3[1] < ul + 1:
            neighbor.add(c3)
        if c4[0] > 0 and c4[0] < ul+1 and c4[1] > 0 and c4[1] < ul + 1:
            neighbor.add(c4)


for (x, y) in neighbor:
    thispoint = True
    for (coord, dist) in sensors:
        if abs(coord[0]-x) + abs(coord[1]-y) <= dist:
            thispoint = False
            break
    if thispoint:
        break


#print(neighbor)

print(x, y)
print(x*4000000+y)
'''

for y in range(0, ul + 1):
    for x in range(0, ul + 1):
        touched = False
        for (coord, dist) in sensors:
            if abs(coord[1] - y) + abs(coord[0] - x) > dist and not touched:
                continue
            touched = True
            break

        if not touched:
            print(x, y)
            print(x*4000000+y)
            exit(0)


print(x,y)
            r = sensor[1] - abs(sensor[0][1] - y)
            for x in range(sensor[0][0]-r, sensor[0][0]+r+1):
                if x >= 0 and x < ul+1:
                    on_line.add(x)
    if len(on_line) < ul+1:
        break

print(len(on_line))
for i in range(0, ul + 1):
    if i in on_line:
        continue
    print(i, y)
    print(i*4000000+y)
    break
'''

# print(on_line)
