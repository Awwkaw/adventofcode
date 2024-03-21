def priority(x):
    return (ord(x) - 96) % 58


team = ['a', 'b', 'c']
k = 0
t1 = 0
t2 = 0

while True:
    try:
        i = input()
    except Exception:
        break

    half = len(i) // 2
    a1 = set(i[:half]) & set(i[half:])
    t1 += priority(a1.pop())

    team[k] = i
    k = (k + 1) % 3

    if k == 0:
        t2 += priority((set(team[0]) & set(team[1]) & set(team[2])).pop())

print(t1)
print(t2)
