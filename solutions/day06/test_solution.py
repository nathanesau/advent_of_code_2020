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


def get_fields(line):
    fields = list(line)
    return fields


def parse_data(data):
    arr, group = [], []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            if group:
                arr.append(group)
            group = []
        else:
            group.append(get_fields(line))
    if group:
        arr.append(group)
    return arr


def test_solution_1_example():
    """
    provided example
    """
    data  = """
    abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b
    """
    arr = parse_data(data)
    s1 = solution_1(arr)
    assert s1 == 11
    print("\nSolution 1 Example: {}".format(s1))


def test_solution_1():
    """
    use input.txt
    """
    data = read_input()
    arr = parse_data(data)
    s1 = solution_1(arr)
    assert s1 == 6170
    print("\nSolution 1: {}".format(s1))


def test_solution_2_example():
    """
    use example data
    """
    data  = """
    abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b
    """
    arr = parse_data(data)
    s2 = solution_2(arr)
    assert s2 == 6
    print("\nSolution 2 Example: {}".format(s2))


def test_solution_2():
    """
    use input.txt
    """
    data = read_input()
    arr = parse_data(data)
    s2 = solution_2(arr)
    assert s2 == 2947
    print("\nSolution 2: {}".format(s2))
