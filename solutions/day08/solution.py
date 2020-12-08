def calculate_accumulator(arr):
    visited = {}
    acc = 0  # accumulator
    index = 0
    while True:
        if index == len(arr):
            break
        command = arr[index]
        action, value = command.split(' ')
        value = int(value)
        if index not in visited:
            visited[index] = True
        else:  # loop
            break
        if action == 'nop':
            index += 1
        elif action == 'acc':
            acc += value
            index += 1
        elif action == 'jmp':  # TODO handle negative index or index >= len(arr)
            index += value
    return acc


def get_ending_index(arr):
    visited = {}
    acc = 0  # accumulator
    index = 0
    while True:
        if index == len(arr):
            return index
        command = arr[index]
        action, value = command.split(' ')
        value = int(value)
        if index not in visited:
            visited[index] = True
        else:  # loop
            break
        if action == 'nop':
            index += 1
        elif action == 'acc':
            acc += value
            index += 1
        elif action == 'jmp':  # TODO handle negative index or index >= len(arr)
            index += value
    return index  # ending index (loop)


def solution_1(arr):
    return calculate_accumulator(arr)


def solution_2(arr):  # brute force
    jmp_indexes = [i for i in range(len(arr)) if arr[i].split(' ')[0] == 'jmp']
    nop_indexes = [i for i in range(len(arr)) if arr[i].split(' ')[0] == 'nop']
    
    found = False
    for jmp_index in jmp_indexes:  # replace 'jmp' with 'nop'
        arr[jmp_index] = arr[jmp_index].replace('jmp', 'nop')
        end = get_ending_index(arr)
        print(end)
        if end == len(arr):
            found = True
            break  # jmp_index was good change!
        arr[jmp_index] = arr[jmp_index].replace('nop', 'jmp') # undo

    if not found:
        raise Exception("Did not implement nop to jmp replace")

    return calculate_accumulator(arr)
