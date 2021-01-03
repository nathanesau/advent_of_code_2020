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
    939
    7,13,x,x,59,x,31,19
    """
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    timestamp = int(lines[0])
    stops = lines[1].split(',')
    s1 = solution_1(timestamp, stops)
    assert s1 == 295


def test_solution_1():
    """
    use input.txt
    """
    data = read_input()
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    timestamp = int(lines[0])
    stops = lines[1].split(',')
    s1 = solution_1(timestamp, stops)
    assert s1 == 3966


def test_solution_2_example():
    """
    provided example
    """
    data = """
    939
    7,13,x,x,59,x,31,19
    """
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    stops = lines[1].split(',')
    s2 = solution_2(stops)
    assert s2 == 1068781


def test_solution_2():
    """
    use input.txt
    """
    data = read_input()
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    stops = lines[1].split(',')
    s2 = solution_2(stops)
    assert s2 == 800177252346225
