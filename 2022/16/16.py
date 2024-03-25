from collections import deque
import itertools


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


def try_paths_share(
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
        path='|AA',
        return_flow=0
        ):

    if start not in visited:
        visited.add(start)
    if to_visit == set():
        return max(max_value, value + m*current_flow), return_flow

    if all([graph[start][end][0]+1 > m or end in visited
            for end in graph[start]]):
        return max(max_value, value + m * current_flow), return_flow

    for end in graph[start]:
        if end in visited:
            continue

        travel, flow = graph[start][end]
        if travel + 1 > m or \
                value +\
                m * current_flow +\
                (m - travel - 1) * max_flow < max_value:
            continue
        test_value, test_return_flow = try_paths_share(
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
                            path[:visit_n*3] + f'|{end}',
                            return_flow
                            )
        if test_value > max_value:
            max_value = test_value
            return_flow = test_return_flow
    return max_value, return_flow


def try_paths_for_two(
        m1,
        m2,
        graph,
        start1,
        start2,
        visited,
        current_flow1,
        current_flow2,
        max_flow,
        value,
        max_value,
        to_visit,
        visit_n1=0,
        visit_n2=0,
        path1='|AA',
        path2='|AA'
        ):

    if start1 not in visited:
        visited.add(start1)
    if start2 not in visited:
        visited.add(start2)
    if to_visit == set():
        print(m1,
              m2,
              current_flow1,
              current_flow2,
              max_flow,value)
        return max(max_value,
                   value + m1*current_flow1 + m2*current_flow2), path1, path2

    print(all([graph[start1][end1][0]+1 > m1 or end1 in visited
               for end1 in graph[start1]]))

    print(all([graph[start2][end2][0]+1 > m2 or end2 in visited
               for end2 in graph[start2]]))

    if all([graph[start1][end1][0]+1 > m1 or end1 in visited
            for end1 in graph[start1]]) and\
            all([graph[start2][end2][0]+1 > m2 or end2 in visited
                 for end2 in graph[start2]]):
        print('hithere')
        return max(max_value,
                   value + m1*current_flow1 + m2*current_flow2), path1, path2

    for end1 in graph[start1]:
        if end1 in visited and len(to_visit) < 2:
            continue
        for end2 in graph[start2]:
            if end1 in visited and end2 in visited:
                continue

        travel1, flow1 = graph[start1][end1]
        travel2, flow2 = graph[start2][end2]
        if travel1 + 1 > m1 and travel2 + 1 > m2:
            continue
        if value +\
                m1 * current_flow1 +\
                m2 * current_flow2 +\
                (max(m1, m2) - (min(travel1, travel2) + 1))*max_flow < max_value:
            continue

        v1 = visit_n1 + 1
        v2 = visit_n2 + 1

        m1_new = m1 - (travel1 + 1)
        m2_new = m2 - (travel2 + 1)
        b1 = False
        b2 = False
        if travel1 + 1 > m1 or end1 == end2 or end1 in visited:
            #print('m1', m1)
            #print(end1)
            #print(travel1 + 1)
            flow1 = 0
            travel1 = -1
            end1 = start1
            v1 = visit_n1
            m1_new = m1
            b1 = True
        if travel2 + 1 > m2 or end2 in visited:
            #print('m2', m2)
            #print(end2)
            #print(travel2 + 1)
            flow2 = 0
            travel2 = -1
            end2 = start2
            v2 = visit_n2
            m2_new = m2
            b2 = True
        if b1 and b2:
            continue
        test_value, test_path1, test_path2 = try_paths_for_two(
                            m1_new,
                            m2_new,
                            graph,
                            end1,
                            end2,
                            visited | {end1, end2},
                            current_flow1 + flow1,
                            current_flow2 + flow2,
                            max_flow,
                            value + current_flow1 * (travel1+1) + current_flow2 * (travel2+1),
                            max(max_value, value),
                            to_visit - {end1, end2},
                            v1,
                            v2,
                            path1[:visit_n1*3] + f'|{end1}',
                            path2[:visit_n2*3] + f'|{end2}'
                            )
        if test_value > max_value:
            max_value = test_value
            path1 = test_path1
            path2 = test_path2
    return max_value, path1, path2

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

#mval = try_paths_for_two(
#        26,
#        26,
#        visit_graph,
#        start,
#        start,
#        {start},
#        0,
#        0,
#        max_pl,
#        0,
#        0,
#        to_visit
#        )
#print(mval)


t2_val = 0
print(len(to_visit))
for i in range(len(to_visit)//2, 0, -1):
    visit_list = to_visit.copy()
    visit_list1 = set()
    visit_list2 = set()
    print(i,flush=True)
    for visit_list1 in itertools.combinations(visit_list, i):
        visit_list1 = set(visit_list1)
        visit_list2 = to_visit - visit_list1
        mval, flow1 = try_paths_share(
                26,
                visit_graph,
                'AA',
                {'AA'} | visit_list2,
                0,
                max_pl,
                0,
                0,
                visit_list1
                )
        if mval + 26*(max_pl) < t2_val:
            continue
        t2_val = max(t2_val,
                     try_paths_share(
                                26,
                                visit_graph,
                                'AA',
                                {'AA'} | visit_list1,
                                0,
                                max_pl,
                                mval,
                                mval,
                                visit_list2,
                                flow1
                                )[0])
print(t2_val)
