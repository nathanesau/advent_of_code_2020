import os
from .solution import (
    solution_1,
    solution_2
)


BASEDIR = os.path.dirname(os.path.abspath(__file__))


def read_input():
    with open("{}/assets/input.txt".format(BASEDIR)) as f:
        data = f.read()
    return data


def test_solution_1_example():
    """
    provided example
    """
    data = """
    16
    10
    15
    5
    1
    11
    7
    19
    6
    12
    4
    """
    arr = [int(line.strip()) for line in data.splitlines() if line.strip()]
    s1 = solution_1(arr)
    assert s1 == 35


def test_solution_1():
    """
    use input.txt
    """
    data = read_input()
    arr = [int(line.strip()) for line in data.splitlines() if line.strip()]
    s1 = solution_1(arr)
    assert s1 == 2232


def test_solution_2_example():
    """
    provided example
    """
    arr = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
    s1 = solution_2(arr)
    assert s1 == 8


def test_solution_2():
    """
    use input.txt
    """
    data = read_input()
    arr = [int(line.strip()) for line in data.splitlines() if line.strip()]
    s2 = solution_2(arr)
    assert s2 == 86812553324672
