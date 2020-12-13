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
    data = """
    28
    33
    18
    42
    31
    14
    46
    20
    48
    47
    24
    23
    49
    45
    19
    38
    39
    11
    1
    32
    25
    35
    8
    17
    7
    9
    4
    2
    34
    10
    3
    """
    arr = [0] + [int(line.strip()) for line in data.splitlines() if line.strip()]
    s2 = solution_2(arr)
    assert s2 == 8


def test_solution_2():
    """
    use input.txt
    """
    data = read_input()
    arr = [0] + [int(line.strip()) for line in data.splitlines() if line.strip()]
    s2 = solution_2(arr)
    assert s2 == 173625106649344
