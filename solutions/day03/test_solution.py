import os
from .solution import (
    solution_1,
    solution_2
)


BASEDIR = os.path.dirname(os.path.abspath(__file__))


def read_input():
    with open("{}/assets/input.txt".format(BASEDIR)) as f:
        data = f.read()
    arr = [list(line.strip()) for line in data.splitlines() if line.strip()]
    return arr


def test_solution_1_example():
    """
    provided example
    """
    data = """
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    """
    arr = [list(line.strip()) for line in data.splitlines() if line.strip()]
    s1 = solution_1(arr)
    assert s1 == 7
    print("\nSolution 1 Example: {}".format(s1))


def test_solution_1():
    """
    use input.txt
    """
    arr = read_input()
    s1 = solution_1(arr)
    assert s1 == 254
    print("\nSolution 1: {}".format(s1))


def test_solution_2_example():
    """
    provided example
    """
    data = """
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    """
    arr = [list(line.strip()) for line in data.splitlines() if line.strip()]
    s2 = solution_2(arr)
    assert s2 == 336
    print("\nSolution 2 Example: {}".format(s2))


def test_solution_2():
    """
    use input.txt
    """
    arr = read_input()
    s2 = solution_2(arr)
    assert s2 == 1666768320
    print("\nSolution 2: {}".format(s2))
