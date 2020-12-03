import os
from functools import reduce
import operator


def find_num_trees(arr, path):
    nrow, ncol = len(arr), len(arr[0])
    pos = [0, 0]
    ntrees = 0
    while pos[0] < nrow:
        pos = [pos[0] + path[0], pos[1] + path[1]]
        if pos[0] < nrow and arr[pos[0]][pos[1] % ncol] == '#':
            ntrees += 1
    return ntrees


def solution_1(arr, path=[1, 3]):
    ntrees = find_num_trees(arr, path)
    return ntrees


def solution_2(arr, paths=[[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]):
    ntrees = []
    for path in paths:
        ntrees.append(find_num_trees(arr, path))
    return reduce(operator.mul, ntrees, 1)
