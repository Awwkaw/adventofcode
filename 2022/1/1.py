import numpy as np
a = [0]
while True:

    try:
        i = input()
    except:
        break
    if i == "":
        a.append(0)
        continue

    a[-1] += int(i)

print(max(a))
a.sort()
print(sum(a[-3:]))
