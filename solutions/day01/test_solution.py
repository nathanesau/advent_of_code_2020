import os
from .solution import (
    solution_1,
    solution_2
)


BASEDIR = os.path.dirname(os.path.abspath(__file__))


def read_input():
    """
    return list of integers corresponding to input
    """
    with open("{}/assets/input.txt".format(BASEDIR)) as f:
        data = f.read()
        return list(map(int, data.splitlines()))


def test_solution_1_example():
    """
    provided example
    """
    s1 = solution_1([1721, 979, 366, 299, 675, 1456])
    assert s1 == 514579
    print("\nSolution 1 Example: {}".format(s1))


def test_solution_1():
    """
    use input.txt
    """
    arr = read_input()
    s1 = solution_1(arr)
    assert s1 == 485739
    print("\nSolution 1: {}".format(s1))


def test_solution_2_example():
    """
    provided example
    """
    s2 = solution_2([1721, 979, 366, 299, 675, 1456])
    assert s2 == 241861950
    print("\nSolution 2 Example: {}".format(s2))


def test_solution_2():
    """
    use input.txt
    """
    arr = read_input()
    s2 = solution_2(arr)
    assert s2 == 161109702
    print("\nSolution 2: {}".format(s2))
