import os
from .solution import (
    solution_1,
    solution_2
)


BASEDIR = os.path.dirname(os.path.abspath(__file__))


def read_input_1():
    """
    interpret first two numbers as min, max
    """
    with open("{}/assets/input.txt".format(BASEDIR)) as f:
        data = f.read()
    a = []
    for policy in data.splitlines():
        mm, char, pwd = policy.split(' ')
        mm = list(map(int, mm.split('-')))
        char = char.split(':')[0]
        a.append({"min": mm[0], "max": mm[1], "char": char, "pwd": pwd})
    return a


def read_input_2():
    """
    interpret first two numbers as pos1, pos2
    """
    with open("{}/assets/input.txt".format(BASEDIR)) as f:
        data = f.read()
    a = []
    for policy in data.splitlines():
        pos, char, pwd = policy.split(' ')
        pos = list(map(int, pos.split('-')))
        char = char.split(':')[0]
        a.append({"p1": pos[0]-1, "p2": pos[1]-1, "char": char, "pwd": pwd})
    return a


def test_solution_1_example():
    """
    provided example
    """
    s1 = solution_1([{"min": 1, "max": 3, "char": "a", "pwd": "abcde"},
                     {"min": 1, "max": 3, "char": "b", "pwd": "cdefg"},
                     {"min": 2, "max": 9, "char": "c", "pwd": "ccccccccc"}])
    assert s1 == 2
    print("\nSolution 1 Example: {}".format(s1))


def test_solution_1():
    """
    use input.txt
    """
    arr = read_input_1()
    s1 = solution_1(arr)
    assert s1 == 396
    print("\nSolution 1: {}".format(s1))


def test_solution_2_example():
    """
    provided example
    """
    s2 = solution_2([{"p1": 1-1, "p2": 3-1, "char": "a", "pwd": "abcde"},
                     {"p1": 1-1, "p2": 3-1, "char": "b", "pwd": "cdefg"},
                     {"p1": 2-1, "p2": 9-1, "char": "c", "pwd": "ccccccccc"}])
    assert s2 == 1
    print("\nSolution 2 Example: {}".format(s2))


def test_solution_2():
    """
    use input.txt
    """
    arr = read_input_2()
    s2 = solution_2(arr)
    assert s2 == 428
    print("\nSolution 2: {}".format(s2))
