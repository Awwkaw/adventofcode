def read_board(board_lines):
    width = len(board_lines[-1].split('['))-1

    board = [[] for i in range(width)]

    idx = [i*4+1 for i in range(width)]
    for line in board_lines[-1::-1]:
        for i, j in enumerate(idx):
            if ord(line[j]) != 32:
                board[i].append(line[j])
    return board


def update_board(board, command):
    split_command = command.split(' ')
    n = int(split_command[1])
    start = int(split_command[3]) - 1
    end = int(split_command[5]) - 1

    for i in range(n):
        board[end].append(board[start].pop())
    return board


def update_board2(board, command):
    split_command = command.split(' ')
    n = int(split_command[1])
    start = int(split_command[3]) - 1
    end = int(split_command[5]) - 1

    for i in range(-n, 0):
        board[end].append(board[start].pop(i))
    return board


def end_line(board):
    res = ''
    for i in range(len(board)):
        res += board[i][-1]
    return res


board_lines = []

while True:
    try:
        i = input()
    except Exception:
        break

    if '[' in i:
        board_lines.append(i)
        continue

    if i == "":
        board = read_board(board_lines)
        board2 = read_board(board_lines)
        continue

    if 'move' not in i:
        continue

    board = update_board(board, i)
    board2 = update_board2(board2, i)

print(end_line(board))
print(end_line(board2))
