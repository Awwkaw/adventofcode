import time
def make_stone(n: int, y0=2, x0=3) -> [list, list]:
    if n % 5 == 0:
        x = [i + x0 for i in range(4)]
        y = [y0 for i in range(4)]
    elif n % 5 == 1:
        x = [1, 0, 1, 2, 1]
        y = [0, 1, 1, 1, 2]
        x = [i + x0 for i in x]
        y = [i + y0 for i in y]
    elif n % 5 == 2:
        x = [0, 1, 2, 2, 2]
        y = [0, 0, 0, 1, 2]
        x = [i + x0 for i in x]
        y = [i + y0 for i in y]
    elif n % 5 == 3:
        x = [x0 for i in range(4)]
        y = [i + y0 for i in range(4)]
    elif n % 5 == 4:
        x = [0, 1, 0, 1]
        y = [0, 0, 1, 1]
        x = [i + x0 for i in x]
        y = [i + y0 for i in y]

    return x, y


gust = list(map(
        int,
        open(0).read().strip().replace('<',
                                       '-1,').replace('>',
                                                      '1,')[:-1].split(',')
        ))

nround = 2022
nround = 1


def run_simul(nround, gust):
    ymax = 0
    yspawn = 4
    stone = {(x, 0) for x in range(8)}
    gust_state = 0
    blocked = [[0, 0], [False, False]]

    for i in range(nround):
        stonex, stoney = make_stone(i, ymax + yspawn)
        while True:
            if not any([
                    (x+gust[gust_state], y) in stone
                    for x, y in zip(stonex, stoney)]) and\
                    not any([x+gust[gust_state] > 7 or x+gust[gust_state] < 1
                             for x in stonex]):
                stonex = [x + gust[gust_state] for x in stonex]
            gust_state = (gust_state + 1) % len(gust)
            if any([
                    (x, y-1) in stone
                    for x, y in zip(stonex, stoney)]):
                break
            stoney = [y-1 for y in stoney]
        for j in range(len(stonex)):
            stone.add((stonex[j], stoney[j]))
            if stoney[j] > ymax:
                ymax = stoney[j]

            if any([x == 0 for x in stonex]):
                blocked[0][0] = min(stoney)
                blocked[1][0] = True
            if any([x == 0 for x in stonex]):
                blocked[0][1] = min(stoney)
                blocked[1][1] = True
            if blocked[1][0] and blocked[1][1]:
                blevel = min(blocked[0])
                for st in stone:
                    if st[1] < blevel:
                        stone.remove(st)
                if blocked[0][1] > blocked[0][0]:
                    blocked[1][0] = False
                else:
                    blocked[0][1] = False
    #print(stonex, stoney)
    return ymax


def run_simul_cycle(nround, gust, fieldstate_len=10):
    ymax = 0
    yspawn = 4
    stone = {(x, 0) for x in range(8)}
    gust_state = 0
    blocked = [[0, 0], [False, False]]
    fieldstates = [[hash(()), 0, 0, 0] for i in range(fieldstate_len)]

    for i in range(nround):
        if i % 1000000 == 0:
            print(i, flush=True)
        stonex, stoney = make_stone(i, ymax + yspawn)
        while True:
            if not any([
                    (x+gust[gust_state], y) in stone
                    for x, y in zip(stonex, stoney)]) and\
                    not any([x+gust[gust_state] > 7 or x+gust[gust_state] < 1
                             for x in stonex]):
                stonex = [x + gust[gust_state] for x in stonex]
            gust_state = (gust_state + 1) % len(gust)
            if any([
                    (x, y-1) in stone
                    for x, y in zip(stonex, stoney)]):
                break
            stoney = [y-1 for y in stoney]

        for j in range(len(stonex)):
            stone.add((stonex[j], stoney[j]))
            if stoney[j] > ymax:
                ymax = stoney[j]

            if any([x == 0 for x in stonex]):
                blocked[0][0] = min(stoney)
                blocked[1][0] = True
            if any([x == 0 for x in stonex]):
                blocked[0][1] = min(stoney)
                blocked[1][1] = True
            if blocked[1][0] and blocked[1][1]:
                blevel = min(blocked[0])
                for st in stone:
                    if st[1] < blevel:
                        stone.remove(st)
                if blocked[0][1] > blocked[0][0]:
                    blocked[1][0] = False
                else:
                    blocked[0][1] = False

        fieldstate = [hash(((x,ymax-y)for x,y in zip(stonex,stoney))), gust_state, ymax, i]
        for state in fieldstates:
            if state[0] == fieldstate[0]\
                    and state[1] == fieldstate[1]\
                    and state[2] < fieldstate[2] - 22\
                    and i > 10*fieldstate_len:
                print(state)
                print(fieldstate)
                noffset = state[3]
                cycleheight = fieldstate[2] - state[2]
                cyclelength = fieldstate[3] - state[3]

                rocks_to_cycle = nround - noffset
                ymax = cycleheight * (rocks_to_cycle // cyclelength)\
                        + run_simul(noffset + rocks_to_cycle % cyclelength, gust) #hiehgt from offset + not fitting in cycles
                return ymax #, noffset, cycleheight, cyclelength
        fieldstates.append(fieldstate)
        if len(fieldstates) > fieldstate_len:
            fieldstates.pop(0)

    # print(stonex, stoney)
    return ymax  #, nround, ymax, nround


print(len(gust)*5)
t1 = run_simul(2022, gust)
print(t1)
n2 = 1000000000000
print(run_simul_cycle(n2, gust, 10000))

'''
tt = time.time()
found_cycle = False
offset = 0
for noffset in range(2022, 10000):
    if not noffset % 10:
        print(noffset, flush=True)
    if noffset != 0:
        offset = run_simul(noffset, gust)
    for cyclelength in range(5, 100):
        l1 = run_simul(noffset+cyclelength, gust) - offset
        for i in range(2, 10):
            ln = run_simul(noffset+cyclelength*i,gust) - offset
            if ln % l1 == 0:
                found_cycle = True
                continue
            else:
                found_cycle = False
                break
        if found_cycle:
            break
    if found_cycle:
        break
2 = 1000000000000
rocks_to_cycle = n2 - noffset
t2 = l1 * (rocks_to_cycle // cyclelength)\
        + run_simul(noffset + rocks_to_cycle % cyclelength, gust)
        #hiehgt from offset + not fitting in cycles

print(offset, l1,(rocks_to_cycle // cyclelength), cyclelength, noffset)
te = time.time()
print(t2, te-tt)
'''
