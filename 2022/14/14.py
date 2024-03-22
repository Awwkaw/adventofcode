
data = open(0).read().splitlines()
for round in range(2):
    xmin = None
    ymin = 0
    xmax = None
    ymax = None


    def grid_simulate(grid, start):
        coord = start
        if grid[start[0]][start[1]] == 'O':
            return grid, None
        while True:
            if coord[0]+1 >= len(grid):
                return grid, None
            elif grid[coord[0]+1][coord[1]] == ' ':
                start = [coord[0], coord[1]]
                coord = [coord[0]+1, coord[1]]
                continue

            if coord[1]-1 < 0:
                return grid, None
            elif grid[coord[0]+1][coord[1]-1] == ' ':
                start = [coord[0], coord[1]]
                coord = [coord[0]+1, coord[1]-1]
                continue

            if coord[1]+1 >= len(grid[0]):
                return grid, None
            elif grid[coord[0]+1][coord[1]+1] == ' ':
                start = [coord[0], coord[1]]
                coord = [coord[0]+1, coord[1]+1]
                continue
            grid[coord[0]][coord[1]] = 'O'
            return grid, start


    def grid_printer(grid):
        for i in range(0, len(grid)):
            print('|', end='')
            for j in range(0, len(grid[i])):
                print(grid[i][j], end='')
            print('|\n', end='')


    for line in data:
        coords = line.split('->')
        for coord in coords:
            x, y = list(map(int, coord.split(',')))
            xmin = min(xmin, x) if xmin is not None else x
            ymin = min(ymin, y) if ymin is not None else y
            xmax = max(xmax, x) if xmax is not None else x
            ymax = max(ymax, y) if ymax is not None else y

    if round == 1:
        ymax = ymax + 2
        xmax = xmax+1000
        xmin = xmin-1000
        data.append(f'{xmin},{ymax} -> {xmax},{ymax}')
    grid = [[' ' for x in range(xmax-xmin+1)] for y in range(ymax-ymin+1)]
    for line in data:
        coords = line.split('->')
        to_draw = []
        for i, coord in enumerate(coords):
            to_draw.append(list(map(int, coord.split(','))))
            #print(to_draw)
            to_draw[i][0] -= xmin
            to_draw[i][1] -= ymin
            if i == 0:
                continue
            if to_draw[i-1][0] == to_draw[i][0]:
                vals = (to_draw[i][1], to_draw[i-1][1])
                y1 = min(vals)
                y2 = max(vals)
                for draw in range(y1, y2 + 1):
                    grid[draw][to_draw[i][0]] = '#'
            else:
                vals = (to_draw[i][0], to_draw[i-1][0])
                x1 = min(vals)
                x2 = max(vals)
                for draw in range(x1, x2 + 1):
                    grid[to_draw[i][1]][draw] = '#'


    grid[0][500-xmin] = '+'
    #grid_printer(grid)
    n = 0
    start = [0, 500-xmin]
    newstart = start
    while True:
        grid, newstart = grid_simulate(grid, start)
        if newstart is not None:
            n += 1
            if grid[newstart[0]][newstart[1]] != ' ':
                newstart = start
        else:
            break

    #grid_printer(grid)
    print(n)
