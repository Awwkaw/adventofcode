import re


def find_options(
        blueprint: list,
        resources: list,
        income: list,
        time: int) -> list:
    options = {'geode': [
                        0,
                        0,
                        [-blueprint[4], 0, -blueprint[5], 0],
                        [0, 0, 0, 1]
                        ],
               'obsidian': [
                        0,
                        0,
                        [-blueprint[2], -blueprint[3], 0, 0],
                        [0, 0, 1, 0]
                        ],
               'clay': [
                        0,
                        0,
                        [-blueprint[1], 0, 0, 0],
                        [0, 1, 0, 0]
                        ],
               'ore': [
                        0,
                        0,
                        [-blueprint[0], 0, 0, 0],
                        [1, 0, 0, 0]
                        ],
               'wait': [
                        0,
                        1,
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        ],
               }

    if resources[0] >= blueprint[4] and\
            resources[2] >= blueprint[5]:
        options['geode'][0] = 1
        options['geode'][1] = 1
    elif income[0] > 0 and income[-2] > 0:
        r2ore = -((blueprint[4] - resources[0]) // -income[0])
        r2obs = -((blueprint[5] - resources[2]) // -income[2])
        options['geode'][1] = max(r2ore, r2obs) + 1
        options['geode'][0] = options['geode'][1] <= time
    if income[0] >= blueprint[4] and income[2] >= blueprint[5]:
        return options

    if resources[0] >= blueprint[2] and\
            resources[1] >= blueprint[3]:
        options['obsidian'][0] = 1
        options['obsidian'][1] = 1
    elif income[0] > 0 and income[1] > 0:
        r2ore = -((blueprint[2] - resources[0]) // -income[0])
        r2cla = -((blueprint[3] - resources[1]) // -income[1])
        options['obsidian'][1] = max(r2ore, r2cla) + 1
        options['obsidian'][0] = options['obsidian'][1] <= time
    if income[2] >= blueprint[5]:
        options['obsidian'][0] = 0

    if resources[0] >= blueprint[1]:
        options['clay'][0] = 1
        options['clay'][1] = 1
    else:
        r2ore = -((blueprint[1] - resources[0]) // -income[0])
        options['clay'][1] = r2ore + 1
        options['clay'][0] = options['clay'][1] <= time
    if income[1] >= blueprint[3]:
        options['clay'][0] = 0

    if resources[0] >= blueprint[0]:
        options['ore'][0] = 1
        options['ore'][1] = 1
    else:
        r2ore = -((blueprint[0] - resources[0]) // -income[0])
        options['ore'][1] = r2ore + 1
        options['ore'][0] = options['ore'][1] <= time
    if income[0] >= max([
                        blueprint[0],
                        blueprint[1],
                        blueprint[2],
                        blueprint[4]]) + 1:
        options['ore'][0] = 0

    if not all([options[key][0] == 0 for key in
                ['geode', 'obsidian', 'clay', 'ore']]):
        options['wait'][0] == 1

    return options


def max_remainder_income(
        time: int,
        ) -> int:
    r = 0
    for i in range(time, -1, -2):
        r += max(0, i)
    return r


def test_blueprint(
        time: int,
        blueprint: list,
        resources: list,
        income: list,
        maxval: int,
        ) -> int:

    options = find_options(
            blueprint,
            resources,
            income,
            time
            )

    if time == 0:
        return max(maxval, resources[-1])

    if (resources[-1]+max_remainder_income(time+2)+income[-1]*(time)) <= maxval:
        # print(time, resources, income)
        return max(maxval, income[-1]*time + resources[-1])

    for key in options.keys():

        option, dt, cost, delin = options[key]
        if not option:
            continue
        if key == 'wait':
            return max(maxval, resources[-1] + income[-1]*time)
        test_value = test_blueprint(
                time - dt,
                blueprint,
                [r + dr + i*dt for r, dr, i in
                 zip(resources, cost, income)],
                [i + di for i, di in zip(income, delin)],
                maxval
                )
        if test_value >= maxval:
            maxval = test_value

    # if resources[-1]:
    #    print(time,resources, options, income)

    return max(maxval, income[-1]*time + resources[-1])


blueprints = []
for line in open(0).read().splitlines():
    a = re.findall(r' \d+ ', line)
    blueprints.append(list(map(int, a)))

#print(blueprints)
br = [0, 0, 0, 0]
bi = [1, 0, 0, 0]

t = 0
for i, blueprint in enumerate(blueprints):
    val = test_blueprint(
        24,
        blueprint,
        br,
        bi,
        0
        )
    print(i+1, val, flush=True)
    t += (i+1)*val

print(t)


t2 = 1
for i, blueprint in enumerate(blueprints):
    if i > 2:
        continue
    val = test_blueprint(
        32,
        blueprint,
        br,
        bi,
        0
        )

    print(i, val, flush=True)
    t2 *= val

print(t2)
