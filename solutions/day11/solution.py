import copy


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print("")
    print("")


def seat_count_adj(grid, i, j):
    """
    return True once count exceeds limit
    return False if count never exceeds limit
    """
    count = 0
    if (i-1) >= 0 and grid[i-1][j] == '#':  # up
        count += 1
    if (i+1) < len(grid) and grid[i+1][j] == '#':  # down
        count += 1
    if (j-1) >= 0 and grid[i][j-1] == '#':  # left
        count += 1
    if (j+1) < len(grid[0]) and grid[i][j+1] == '#':  # right
        count += 1
    if (i-1) >= 0 and (j-1) >= 0 and grid[i-1][j-1] == '#':  # up-left
        count += 1
    if (i+1) < len(grid) and (j+1) < len(grid[0]) and grid[i+1][j+1] == '#':  # down-right
        count += 1
    if (i+1) < len(grid) and (j-1) >= 0 and grid[i+1][j-1] == '#':  # down-left
        count += 1
    if (i-1) >= 0 and (j+1) < len(grid[0]) and grid[i-1][j+1] == '#':  # up-right
        count += 1
    return count


def shuffle_seats_adj(grid):
    """
    return True if grid was changed False otherwise
    """
    adj = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                continue
            if grid[i][j] == 'L' and seat_count_adj(grid, i, j) == 0:
                adj[(i, j)] = '#'
            if grid[i][j] == '#' and seat_count_adj(grid, i, j) >= 4:
                adj[(i, j)] = 'L'
    for k, v in adj.items():
        grid[k[0]][k[1]] = v
    return True if adj else False


def solution_1(grid):
    while shuffle_seats_adj(grid):
        continue
    return sum(row.count('#') for row in grid)


def get_first_seat_left(grid, i, j):
    col = j - 1
    while col >= 0:
        if grid[i][col] != '.':
            return grid[i][col]
        col -= 1
    return None


def get_first_seat_right(grid, i, j):
    col = j + 1
    while col <= len(grid[0]) - 1:
        if grid[i][col] != '.':
            return grid[i][col]
        col += 1
    return None


def get_first_seat_up(grid, i, j):
    row = i - 1
    while row >= 0:
        if grid[row][j] != '.':
            return grid[row][j]
        row -= 1
    return None


def get_first_seat_down(grid, i, j):
    row = i + 1
    while row <= len(grid) - 1:
        if grid[row][j] != '.':
            return grid[row][j]
        row += 1
    return None


def get_first_seat_up_left(grid, i, j):
    row = i - 1
    col = j - 1
    while row >=0 and col >= 0:
        if grid[row][col] != '.':
            return grid[row][col]
        row -= 1
        col -= 1
    return None


def get_first_seat_down_right(grid, i, j):
    row = i + 1
    col = j + 1
    while row <= len(grid) - 1 and col <= len(grid[0]) - 1:
        if grid[row][col] != '.':
            return grid[row][col]
        row += 1
        col += 1
    return None


def get_first_seat_up_right(grid, i, j):
    row = i - 1
    col = j + 1
    while row >= 0 and col <= len(grid[0]) - 1:
        if grid[row][col] != '.':
            return grid[row][col]
        row -= 1
        col += 1
    return None


def get_first_seat_down_left(grid, i, j):
    row = i + 1
    col = j - 1
    while row <= len(grid) - 1 and col >= 0:
        if grid[row][col] != '.':
            return grid[row][col]
        row += 1
        col -= 1
    return None


def seat_count_vis(grid, i, j):
    """
    return True once count exceeds limit
    return False if count never exceeds limit
    """
    count = 0
    if get_first_seat_up(grid, i, j) == '#':  # up
        count += 1
    if get_first_seat_down(grid, i, j) == '#':  # down
        count += 1
    if get_first_seat_left(grid, i, j) == '#':  # left
        count += 1
    if get_first_seat_right(grid, i, j) == '#':  # right
        count += 1
    if get_first_seat_up_left(grid, i, j) == '#':  # up-left
        count += 1
    if get_first_seat_down_right(grid, i, j) == '#':  # down-right
        count += 1
    if get_first_seat_down_left(grid, i, j) == '#':  # down-left
        count += 1
    if get_first_seat_up_right(grid, i, j) == '#':  # up-right
        count += 1
    return count


def shuffle_seats_vis(grid):
    """
    return True if grid was changed False otherwise
    """
    adj = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                continue
            if grid[i][j] == 'L' and seat_count_vis(grid, i, j) == 0:
                adj[(i,j)] = '#'
            if grid[i][j] == '#' and seat_count_vis(grid, i, j) >= 5:
                adj[(i, j)] = 'L'
    for k, v in adj.items():
        grid[k[0]][k[1]] = v
    return True if adj else False


def solution_2(grid):
    while shuffle_seats_vis(grid):
        continue
    return sum(row.count('#') for row in grid)
