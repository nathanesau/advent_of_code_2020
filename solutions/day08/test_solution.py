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
    nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6
    """
    arr = [line.strip() for line in data.splitlines() if line.strip()]
    s1 = solution_1(arr)
    assert s1 == 5


def test_solution_1():
    """
    use input.txt
    """
    data = read_input()
    arr = [line.strip() for line in data.splitlines() if line.strip()]
    s1 = solution_1(arr)
    assert s1 == 1915


def test_solution_2_example():
    data = """
    nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6
    """
    arr = [line.strip() for line in data.splitlines() if line.strip()]
    s2 = solution_2(arr)
    assert s2 == 8


def test_solution_2():
    """
    use input.txt
    """
    data = read_input()
    arr = [line.strip() for line in data.splitlines() if line.strip()]
    s2 = solution_2(arr)
    assert s2 == 944
