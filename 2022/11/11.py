import numpy as np
data = open(0).read().splitlines()

funcs = {
        '*': lambda x, y: x*y,
        '+': lambda x, y: x+y,
         }

monkey_n = (len(data) + 1) // 7
items = []

tests = []
vals = []
symbs = []
a = []
b = []
f = []


def test_func(a, b, val, fac):
    if val % fac == 0:
        return a
    return b


def reduce_worry(val, fac):
    if val % fac == 0:
        return val // fac
    return val


def op(old, val, symbol):
    if val == 'old':
        val = old
    val = int(val)
    if symbol == '+':
        return old + val
    if symbol == '*':
        return old * val


for monkey in range(monkey_n):
    monkey_line = monkey * 7

    items.append([int(i) for i in
                  data[monkey_line + 1].split(':')[-1].split(',')])
    operation_text = data[monkey_line + 2].split(' ')
    symbs.append(operation_text[-2])
    vals.append(operation_text[-1])

    f.append(int(data[monkey_line+3].split(' ')[-1]))
    a.append(int(data[monkey_line+4].split(' ')[-1]))
    b.append(int(data[monkey_line+5].split(' ')[-1]))

    tests.append(lambda x:
                 a[monkey] if ((x % f[monkey]) == 0) else b[monkey])

k = 2
for factor in f:
    k *= factor

inspected = [0 for i in range(monkey_n)]

for round in range(10000):
    for monkey in range(monkey_n):
        for i in range(len(items[monkey])):
            worry = items[monkey].pop(0)
            worry = op(worry, vals[monkey], symbs[monkey]) % k # change loop to range(20) and % k to // 3 for round 1
            items[test_func(
                    a[monkey],
                    b[monkey],
                    worry,
                    f[monkey]
                    )].append(worry)
            inspected[monkey] += 1


print(inspected.pop(np.argmax(inspected))*inspected.pop(np.argmax(inspected)))


### 
