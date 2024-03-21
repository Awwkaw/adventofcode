def full_overlap(a, b):
    r = 0
    if a[0] <= b[0] and a[1] >= b[1]:
        r = 1
    elif b[0] <= a[0] and b[1] >= a[1]:
        r = 1
    return r


def overlap(a, b):
    r = 0
    if a[0] >= b[0] and a[0] <= b[1]:
        r = 1
    elif b[0] >= a[0] and b[0] <= a[1]:
        r = 1
    return r


t1 = 0
t2 = 0
t3 = 0
while True:
    try:
        i = input()
    except Exception:
        break
    a, b = [[int(r.split('-')[0]), int(r.split('-')[1])] for r in i.split(',')]

    t1 += full_overlap(a, b)
    t2 += overlap(a, b)

print(t1)
print(t2)
