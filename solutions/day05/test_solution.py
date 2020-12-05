import os
from .solution import (
    solution_1,
    solution_2
)


BASEDIR = os.path.dirname(os.path.abspath(__file__))


def read_input():
    with open("{}/assets/input.txt".format(BASEDIR)) as f:
        data = f.read()
    return [list(line.strip()) for line in data.splitlines()]


def test_solution_1_example():
    """
    provided example
    """
    data = list(map(list, ["FBFBBFFRLR", "FFFBBBFRRR", "BBFFBBFRLL"]))
    s1 = solution_1(data)
    assert s1 == 820
    print("\nSolution 1 Example: {}".format(s1))


def test_solution_1():
    """
    use input.txt
    """
    arr = read_input()
    s1 = solution_1(arr)
    # assert s1 == 357
    print("\nSolution 1: {}".format(s1))


def test_solution_2():
    """
    it doesn't make sense to use example data for this
    """
    arr = read_input()
    s1 = solution_2(arr)
    #assert s1 == 820
    print("\nSolution 1 Example: {}".format(s1))
