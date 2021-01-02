import os
import pytest
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
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    """
    grid = [list(line.strip()) for line in data.splitlines() if line.strip()]
    s1 = solution_1(grid)
    assert s1 == 37


def test_solution_1():
    """
    use input.txt
    """
    data = read_input()
    grid = [list(line.strip()) for line in data.splitlines() if line.strip()]
    s1 = solution_1(grid)
    assert s1 == 2361


def test_solution_2_example():
    """
    provided example
    """
    data = """
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
    """
    grid = [list(line.strip()) for line in data.splitlines() if line.strip()]
    s2 = solution_2(grid)
    assert s2 == 26


def test_solution_2():
    """
    use input.txt
    """
    data = read_input()
    grid = [list(line.strip()) for line in data.splitlines() if line.strip()]
    s2 = solution_2(grid)
    assert s2 == 2119
