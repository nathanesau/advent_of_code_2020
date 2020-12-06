# Day 6

1. Get total number of unique responses to questions within each group.
Sum these totals.

2. Get total number of common responses to questions within each group.
Sum these totals.


```python
# ex. data  = """
#             abc
#
#             a
#             b
#             c
#             """
def parse_data(data) -> list: # [['a', 'b', 'c'], [['a','b'],['a', 'c']], ...]
    arr = []
    group = []
    for line in data.splitlines():
        line = line.strip()
        if line:
            group.append(list(line))
        else:
            if group:
                arr.append(group)
            group = []
    if group:
        arr.append(group)
    return arr

def solution_1(arr):
    total = 0
    for group in arr:
        group_list = []
        for person in group:
            group_list = group_list + person
        group_set = set(group_list)
        total += len(group_set)
    return total

from collections import Counter
def solution_2(arr):
    total = 0
    for group in arr:
        group_list = []
        for person in group:
            group_list = group_list + person
        group_table = Counter(''.join(group_list))
        for k, v in group_table.items():
            if v == len(group):
                total += 1
    return total
```