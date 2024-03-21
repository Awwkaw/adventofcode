
ops = {'noop': 1, 'addx': 2}
cycle = 0
wait = 0
arg = 0
buffer = 1
t1 = 0
screen = ''

while True:
    if wait > 0:
        if abs(buffer - ((cycle - 0) % 40)) < 2:
            screen += 'Ø'
        else:
            screen += ' '
        cycle += 1
        if not (cycle - 20) % 40:
            t1 += cycle * buffer
        wait -= 1
        if wait == 0:
            buffer += arg
            arg = 0
        continue

    try:
        i = input()
    except Exception:
        break
    op = i.split()[0]

    wait = ops[op]

    if op == 'addx':
        arg = int(i.split()[1])

print(t1)

print('')

for i in range(0, len(screen), 40):
    print(screen[i:i+40])
