# Day 8

1. Execute instructions (nop, acc, jmp). 
   Calculate value of accumulator.
   Code terminates after one loop iteration.

2. Change one line of code to prevent loop.
   Change a jmp command to a nop command.
   
   
```python
# ex. arr = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3"
#            "acc -99", "acc +1", "jmp -4", "acc +6"]
def solution_1(arr):
    visited = {}
    acc = 0
    index = 0
    while True:
        if index in visited: # looping
            return acc
        command = arr[index]
        action, value = command.split(' ')
        value = int(value)
        if action == 'nop' or 'acc':
            index += 1
            if action == 'acc':
                acc += value
        elif action == 'jmp':
            index += value
    return None

def find_ending_index(arr):
    visited = {}
    acc = 0
    index = 0
    while True:
        if index == len(arr):
            return index
        if index in visited: # looping
            return index
        command = arr[index]
        action, value = command.split(' ')
        value = int(value)
        if action == 'nop' or 'acc':
            index += 1
            if action == 'acc':
                acc += value
        elif action == 'jmp':
            index += value
    return None

# ex. arr = ["nop +0", "acc +1", "jmp +4", "acc +3", "jmp -3"
#            "acc -99", "acc +1", "jmp -4", "acc +6"]
def solution_2(arr):
    """
    Need to figure out which command to change.
    Try all possible jmp commands and determine ending index.
    """
    jmp_indexes = [i for in range(len(arr)) if arr[i].split(' ')[0] == 'jmp']
    for jmp_index in jmp_indexes:
        arr[jmp_index] = arr[jmp_index].replace('jmp', 'nop')
        end_index = find_ending_index(arr)
        if end_index == len(arr):  # jmp to nop was a good change
            return solution_1(arr)
        arr[jmp_index] = arr[jmp_index].replace('nop', 'jmp') # revert try next
    return None
```