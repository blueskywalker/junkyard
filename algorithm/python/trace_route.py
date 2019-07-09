
board = [
    ['A', 'G', 'F', 'Z', 'H'],
    ['B', 'D', 'C', 'X', 'P'],
    ['E', 'Y', 'A', 'R', 'W'],
    ['B', 'C', 'N', 'M', 'Q']
]


start_point={}
rows=0
columns=0

def build_start_point(board):
    global start_point
    global rows, columns
    rows = len(board)
    if rows == 0:
        return

    columns = len(board[0])

    for row in range(rows):
        for column in range(columns):
            key_char = board[row][column]
            if key_char in start_point:
                start_point[key_char].append((row, column))
            else:
                start_point[key_char] = [(row, column)]


build_start_point(board)


def trace_char(query, step, location, route):
    if len(query)-1 == step:
        return True

    x, y = location
    if board[x][y] != query[step]:
        return False

    new_location = ( x + 1, y )
    if x+1 < rows and new_location not in route and board[x+1][y] == query[step+1]:
        result = trace_char(query, step+1, new_location, route | set([location]))
        if result:
            return True
    new_location = ( x - 1, y )
    if x-1 > -1 and new_location not in route and board[x-1][y] == query[step+1]:
        result = trace_char(query, step+1, new_location, route | set([location]))
        if result:
            return True

    new_location = ( x, y + 1 )
    if y+1 < columns and new_location not in route and board[x][y+1] == query[step+1]:
        result = trace_char(query, step+1, new_location, route | set([location]))
        if result:
            return True

    new_location = ( x, y - 1 )
    if y-1 > -1 and new_location not in route and board[x][y-1] == query[step+1]:
        result = trace_char(query, step+1, new_location, route | set([location]))
        if result:
            return True

    return False


def is_exist(query):
    if len(query) == 0:
        return False

    start_char = query[0]

    if start_char in start_point:
        for location in start_point[start_char]:
            if trace_char(query, 0, location, set()):
                return True

    return False



query='ACFZHP'
print(is_exist(query))
