def solution_1(arr, initial_dir="E"):
    pos = [0, 0] # x, y
    dir = initial_dir
    for move in arr:
        type, value = move[0], int(move[1:])
        if type == 'F':
            pos = [pos[0] + value, pos[1]] if dir == 'E' else [pos[0] - value, pos[1]] if dir == 'W' else \
                [pos[0], pos[1] + value] if dir == 'N' else [pos[0], pos[1] - value]
        if type == 'E':
            pos = [pos[0] + value, pos[1]]
        if type == 'W':
            pos = [pos[0] - value, pos[1]]
        if type == 'N':
            pos = [pos[0], pos[1] + value]
        if type == 'S':
            pos = [pos[0], pos[1] - value]
        if type == 'R':  # clockwise
            order = ['E', 'S', 'W', 'N']
            shift = value % 360 // 90
            index = order.index(dir)
            dir = order[(index + shift) % 4]
        if type == 'L':  # counter-clockwise
            order = ['E', 'N', 'W', 'S']
            shift = value % 360 // 90
            index = order.index(dir)
            dir = order[(index + shift) % 4]
    return abs(pos[0]) + abs(pos[1])


def rotate_cw(pos, value):
    dir = 'E' if pos[0] > 0 else 'W' if pos[0] < 0 else 'N' if pos[1] > 0 else 'S'
    order = ['E', 'S', 'W', 'N']
    shift = value % 360 // 90
    index = order.index(dir)
    dir = order[(index + shift) % 4]
    pv = abs(pos[0]) + abs(pos[1])
    return [pv, 0] if dir == 'E' else [-pv, 0] if dir == 'W' else [0, pv] if dir == 'N' else [0, -pv]


def rotate_ccw(pos, value):
    dir = 'E' if pos[0] > 0 else 'W' if pos[0] < 0 else 'N' if pos[1] > 0 else 'S'    
    order = ['E', 'N', 'W', 'S']
    shift = value % 360 // 90
    index = order.index(dir)
    dir = order[(index + shift) % 4]
    pv = abs(pos[0]) + abs(pos[1])
    return [pv, 0] if dir == 'E' else [-pv, 0] if dir == 'W' else [0, pv] if dir == 'N' else [0, -pv]


def rotate(pos, type, value):
    if type == 'R':
        p1 = rotate_cw([pos[0], 0], value)
        p2 = rotate_cw([0, pos[1]], value)
    if type == 'L':
        p1 = rotate_ccw([pos[0], 0], value)
        p2 = rotate_ccw([0, pos[1]], value)
    return [p1[0] + p2[0], p1[1] + p2[1]]


def solution_2(arr, initial_wp=[10, 1]):
    pos = [0, 0] # x, y
    wp = initial_wp
    for move in arr:
        type, value = move[0], int(move[1:])
        if type == 'F':
            pos = [pos[0] + value * wp[0], pos[1] + value * wp[1]]
        if type == 'E':
            wp = [wp[0] + value, wp[1]]
        if type == 'W':
            wp = [wp[0] - value, wp[1]]
        if type == 'N':
            wp = [wp[0], wp[1] + value]
        if type == 'S':
            wp = [wp[0], wp[1] - value]
        if type == 'R':  # clockwise
            wp = rotate(wp, type, value)
        if type == 'L':  # counter-clockwise
            wp = rotate(wp, type, value)
    return abs(pos[0]) + abs(pos[1])
