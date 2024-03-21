import numpy as np


def get_treemap(data):
    height = len(data)
    width = len(data[0])
    trees = np.zeros((height, width), np.uint8)
    for i, line in enumerate(data):
        trees[i, :] = np.array([int(k) for k in list(line)])
    return trees


def dirscore(trees):
    score = 0
    for tree in trees:
        score += 1
        if tree:
            break

    return score


data = open(0).read().splitlines()
trees = get_treemap(data)
t1 = (trees.shape[0] + trees.shape[1] - 2) * 2
t2 = 0

for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        u = trees[i, :j] >= trees[i, j]
        d = trees[i, j+1:] >= trees[i, j]
        m = trees[:i, j] >= trees[i, j]
        r = trees[i+1:, j] >= trees[i, j]
        if np.min([
                np.sum(u),
                np.sum(d),
                np.sum(m),
                np.sum(r)
                ]) == 0:
            pass
        else:
            continue
        t1 += 1
        ku = dirscore(u[::-1])
        kd = dirscore(d)
        km = dirscore(m[::-1])
        kr = dirscore(r)
        t2 = max(t2, ku * kd * km * kr)


print(t1)
print(t2)
