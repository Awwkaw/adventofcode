
lu1 = {'A': 0,
       'B': 1,
       'C': 2}

lu2 = {'X': 0,
       'Y': 1,
       'Z': 2}

score1 = 0
score2 = 0
for i in open(0).read().splitlines():
    a = lu1[i[0]]
    b = lu2[i[-1]]

    # Assumed score
    if a == b:
        score1 += 3
    elif (b - a) % 3 == 1:
        score1 += 6
    score1 += b + 1

    # Actual score
    score2 += b * 3
    score2 += (a + (b - 1)) % 3 + 1

print(score1)
print(score2)
