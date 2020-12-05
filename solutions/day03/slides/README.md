# Day 3

1. find number of trees encountered on a course using a certain path.

2. find number of trees encountered on a course using several paths.
multiply the number of trees together.

```python
# part 1
# ex. data = """..##.........##.......
#               #...#...#..#...#...#..
#               .#....#..#..#....#..#.
#               ..#.#...#.#..#.#...#.#"""
def solution_1(arr, path=[1, 3]):
    ntrees = 0
    pos = [0,0]
    nrow, ncol = len(arr), len(arr[0])
    while pos[0] < nrow:
        pos = [pos[0] + path[0], pos[1] + path[1]]
        if pos[0] < nrow and arr[pos[0]][pos[1]%ncol] == '#':
            ntrees += 1
    return ntrees

def get_num_trees(arr, path):
    ntrees = 0
    pos = [0,0]
    nrow, ncol = len(arr), len(arr[0])
    while pos[0] < nrow:
        pos = [pos[0] + path[0], pos[1] + path[1]]
        if pos[0] < nrow and arr[pos[0]][pos[1]%ncol] == '#':
            ntrees += 1
    return ntrees

# part 2
# ex. data = """..##.......
#               #...#...#..
#               .#....#..#.
#               ..#.#...#.#"""
from functools import reduce
import operator
def solution_2(arr, paths=[[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]):
    ntrees = []
    for path in paths:
        ntrees.append(get_num_trees(arr, path))
    return reduce(operator.mul, ntrees, 1)
```