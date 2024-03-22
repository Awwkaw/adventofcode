def compare(v, r):
    # print(v, r)
    if isinstance(v, int) and isinstance(r, int):
        if v < r:
            return 1
        elif v > r:
            return 0
    if isinstance(v, list) and isinstance(r, list):
        if v == [] and r != []:
            return 1
        elif v != [] and r == []:
            return 0
        for i in range(len(v)):
            if i >= len(r):
                return 0
            val = compare(v[i], r[i])
            if val is not None:
                return val
        if len(r) > len(v):
            return 1

    if isinstance(v, int) and isinstance(r, list):
        return compare([v], r)

    if isinstance(v, list) and isinstance(r, int):
        return compare(v, [r])


def sort_fun(values):
    if len(values) == 1:
        return values
    pivot = len(values) // 2
    pre = []
    post = []
    piv = [values.pop(pivot)]
    for value in values:
        test = compare(value, piv[0])
        if test == 1:
            pre.append(value)
        if test == 0:
            post.append(value)
    if not pre == []:
        pre = sort_fun(pre)
    if not post == []:
        post = sort_fun(post)
    return pre + piv + post


pairs = []
t1 = 0

data = open(0).read()

for i, pair in enumerate(data.split('\n\n')):
    # if i != 3:
    #     continue
    # print((i+1)*compare(eval(pair.split('\n')[0]), eval(pair.split('\n')[1])))
    t1 += (i+1)*compare(eval(pair.split('\n')[0]), eval(pair.split('\n')[1]))

print(t1)

data += '\n[[2]]\n[[6]]'

decoders = [[[2]], [[6]]]
t2 = 1
lines = []
for i, line in enumerate(data.replace('\n\n', '\n').split('\n')):
    lines.append(eval(line))

for i, line in enumerate(sort_fun(lines)):
    if line in decoders:
        t2 *= i + 1

print(t2)
