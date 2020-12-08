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
    data  = """
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """
    s1 = solution_1(data)
    assert s1 == 4
    print("\nSolution 1 Example: {}".format(s1))


def test_solution_1():
    """
    use input.txt
    """
    data = read_input()
    s1 = solution_1(data)
    assert s1 == 316
    print("\nSolution 1: {}".format(s1))


def test_solution_2_example():
    """
    provided example
    """
    data = """
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """
    s2 = solution_2(data)
    assert s2 == 32
    print("\nSolution 2 Example: {}".format(s2))


def test_solution_2():
    """
    use input.txt
    """
    data = read_input()
    s2 = solution_2(data)
    assert s2 == 11310
    print("\nSolution 2: {}".format(s2))
