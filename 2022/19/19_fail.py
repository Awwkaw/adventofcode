import re


def find_options(
        blueprint: list,
        resources: list,
        income: list,
        building: bool) -> list:
    options = [0, 0, 0, 0, 1]

    if building:
        return options

    if resources[0] >= blueprint[4] and\
            resources[2] >= blueprint[5]:
        options[0] = 1

    if resources[0] >= blueprint[2] and\
            resources[1] >= blueprint[3]:#\
            #and income[2] < blueprint[5]:
        options[1] = 1

    if resources[0] >= blueprint[1]:\
            #and income[1] < blueprint[3]:
        options[2] = 1

    if resources[0] >= blueprint[0]:#\
            #and income[0] < max([blueprint[k] for k in [0, 1, 2, 4]]):
        options[3] = 1

    return options


def max_remainder_income(
        time: int,
        ) -> int:
    r = 0
    for i in range(time, -1, -2):
        r += max(0, i-1)
    return r


def resource_loss(
        idx: int,
        blueprint: list) -> list:
    dr = [0, 0, 0, 0]
    if idx == 3:
        dr[0] -= blueprint[0]
    if idx == 2:
        dr[0] -= blueprint[1]
    if idx == 1:
        dr[0] -= blueprint[2]
        dr[1] -= blueprint[3]
    if idx == 0:
        dr[0] -= blueprint[4]
        dr[2] -= blueprint[5]
    return dr


def test_blueprint(
        time: int,
        blueprint: list,
        resources: list,
        income: list,
        maxval: int,
        building: bool,
        ) -> int:

    options = find_options(
            blueprint,
            resources,
            income,
            building
            )

    if time == 0:
        return max(maxval, resources[-1])

    if (resources[-1]+max_remainder_income(time)+income[-1]*time) * 2 < maxval:
        return maxval

    # if options[0] == 1:
        # print(time, options, resources, income)
    # resources = [r + i for r, i in zip(resources, income)]
    for i, option in enumerate(options):

        if not option:
            continue
        if i == 4:
            building = False
        else:
            building = True

        test_value = test_blueprint(
                time-1,
                blueprint,
                [r+dr+v for r, dr, v in
                 zip(resources, resource_loss(i, blueprint), income)],
                [k + 1 if j == abs(i-3) and i != 4 else k
                 for j, k in enumerate(income)],
                maxval,
                building,
                )
        if test_value >= maxval:
            maxval = test_value

    # if resources[-1]:
    #    print(time,resources, options, income)

    return max(maxval, resources[-1] + income[-1]*time)


blueprints = []
for line in open(0).read().splitlines():
    a = re.findall(r' \d+ ', line)
    blueprints.append(list(map(int, a)))

print(blueprints)
br = [0, 0, 0, 0]
bi = [1, 0, 0, 0]


val = test_blueprint(
    24,
    blueprints[1],
    br,
    bi,
    0,
    False)

print(val)


for i in range(5):
    print(resource_loss(i, blueprints[1]))
