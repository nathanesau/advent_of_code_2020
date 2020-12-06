import os
from collections import Counter


def solution_1(arr):
    total = 0
    for group in arr:
        group_list = []
        for person in group:
            group_list = group_list + person
        group_set = set(group_list)
        total += len(group_set)
    return total


def solution_2(arr):
    """
    return number of responses which everyone within a group had in common
    """
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
