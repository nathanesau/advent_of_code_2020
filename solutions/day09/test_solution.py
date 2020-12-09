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
    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576
    """
    arr = [int(line.strip()) for line in data.splitlines() if line.strip()]
    s1 = solution_1(arr, preamble=5)
    assert s1 == 127


def test_solution_1():
    """
    use input.txt
    """
    data = read_input()
    arr = [int(line.strip()) for line in data.splitlines() if line.strip()]
    s1 = solution_1(arr, preamble=25)
    assert s1 == 2089807806


def test_solution_2_example():
    """
    provided example
    """
    data = """
    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576
    """
    arr = [int(line.strip()) for line in data.splitlines() if line.strip()]
    s1 = solution_2(arr, target=127)
    assert s1 == 62


def test_solution_2():
    data = read_input()
    arr = [int(line.strip()) for line in data.splitlines() if line.strip()]
    s2 = solution_2(arr, target=2089807806)
    assert s2 == 2089807806
