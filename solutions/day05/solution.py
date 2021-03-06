def get_row(bp):
    lower, upper = 0, 127
    for char in bp[0:7]:
        mid = (lower + upper) // 2
        if char == 'F':  # keep lower half
            upper = mid
        elif char == 'B':  # keep upper half
            lower = mid + 1  # +1 because mid is always odd
    return lower  # lower and upper are same


def get_col(bp):
    lower, upper = 0, 7
    for char in bp[7:]:
        mid = (lower + upper) // 2
        if char == 'L':  # keep lower half
            upper = mid
        elif char == 'R':  # keep upper half
            lower = mid + 1  # +1 because mid is always odd
    return lower  # lower and upper are same


def solution_1(arr):
    max_seat_id = 0
    for bp in arr:
        row, col = get_row(bp), get_col(bp)
        seat_id = row * 8 + col
        max_seat_id = max(max_seat_id, seat_id)
    return max_seat_id


def solution_2(arr):
    seat_set = set()
    for bp in arr:
        row, col = get_row(bp), get_col(bp)
        seat_id = row * 8 + col
        seat_set.add(seat_id)
    for seat_id in range(min(seat_set), max(seat_set), 1):
        if seat_id not in seat_set:
            return seat_id
    return None
