from collections import deque


def find_path_length(graph, start, end):
    path = deque([[start, 0]])
    visited = set(start)
    n = 0
    while True:
        coord, n = path.popleft()
        if coord == end:
            return n
        for p in graph[coord][1]:
            if p not in visited:
                path.append([p, n+1])
                visited.add(p)


def try_paths(
        m,
        graph,
        start,
        visited,
        current_flow,
        max_flow,
        value,
        max_value,
        to_visit,
        visit_n=0,
        path='|AA'
        ):

    if start not in visited:
        visited.add(start)
    if to_visit == set():
        return max(max_value, value + m*current_flow), path
    if all([graph[start][end][0]+1 > m or end in visited
            for end in graph[start]]):
        return max(max_value, value + m * current_flow), path
    for end in graph[start]:
        if end in visited:
            continue

        travel, flow = graph[start][end]
        if travel + 1 > m or \
                value +\
                m * current_flow +\
                (m - travel - 1) * max_flow < max_value:
            continue
        test_value, test_path = try_paths(
                            m - (travel + 1),
                            graph,
                            end,
                            visited | {end},
                            current_flow + flow,
                            max_flow,
                            value + current_flow * (travel+1),
                            max(max_value, value),
                            to_visit - {end},
                            visit_n + 1,
                            path[:visit_n*3] + f'|{end}'
                            )
        if test_value > max_value:
            max_value = test_value
            path = test_path
    return max_value, path


graph = {}
for line in open(0).read().splitlines():
    graph[line[6:8]] = [
            int(line.split('=')[1].split(';')[0]),
            [c[0:2] for c in line.split('valv')[1].split(' ')[1:]]
            ]


start = 'AA'
visit_graph = {}
for g in graph:
    if g == start or graph[g][0] > 0:
        visit_graph[g] = {}
        for to in graph:
            if to == g:
                continue
            if graph[to][0] > 0:
                visit_graph[g][to] = [
                        find_path_length(graph, g, to),
                        graph[to][0]
                        ]

to_visit = set()
for g in graph:
    if graph[g][0] > 0:
        to_visit.add(g)

m = 30
pl = []
max_pl = sum([x[0] for x in graph.values()])

mval = try_paths(
        m,
        visit_graph,
        start,
        {start},
        0,
        max_pl,
        0,
        0,
        to_visit
        )
print(mval)
