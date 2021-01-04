import os
from .solution import (
    solution_1,
    solution_2
)


BASEDIR = os.path.dirname(os.path.realpath(__file__))


def read_input():
    with open(f"{BASEDIR}/assets/input.txt") as f:
        data = f.read()
    return data


def test_solution_1_example():
    """
    provided example
    """
    data = """
    F10
    N3
    F7
    R90
    F11
    """
    arr = [line.strip() for line in data.splitlines() if line.strip()]
    s1 = solution_1(arr)
    assert s1 == 25


def test_solution_1():
    """
    use input.txt
    """
    data = read_input()
    arr = [line.strip() for line in data.splitlines() if line.strip()]
    s1 = solution_1(arr)
    assert s1 == 858


def test_solution_2_example():
    """
    provided example
    """
    data = """
    F10
    N3
    F7
    R90
    F11
    """
    arr = [line.strip() for line in data.splitlines() if line.strip()]
    s2 = solution_2(arr)
    assert s2 == 286


def test_solution_2():
    """
    use input.txt
    """
    data = read_input()
    arr = [line.strip() for line in data.splitlines() if line.strip()]
    s2 = solution_2(arr)
    assert s2 == 39140
