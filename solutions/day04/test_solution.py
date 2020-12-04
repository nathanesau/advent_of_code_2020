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


def get_fields(passport):
    fields = []
    for passport_line in passport:
        fields = fields + passport_line.split(' ')
    return fields


def parse_data(data):
    arr, passport = [], []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            if passport:
                arr.append(get_fields(passport))
            passport = []
        else:
            passport.append(line)
    if passport:
        arr.append(get_fields(passport))
    return arr


def test_solution_1_example():
    """
    provided example
    """
    data = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in
    """
    arr = parse_data(data)
    s1 = solution_1(arr)
    assert s1 == 2
    print("\nSolution 1 Example: {}".format(s1))


def test_solution_1():
    """
    use input.txt
    """
    data = read_input()
    arr = parse_data(data)
    s1 = solution_1(arr)
    assert s1 == 235
    print("\nSolution 1: {}".format(s1))


def test_solution_2_example():
    """
    provided example
    """
    data = """
    pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
    hcl:#623a2f

    eyr:2029 ecl:blu cid:129 byr:1989
    iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

    hcl:#888785
    hgt:164cm byr:2001 iyr:2015 cid:88
    pid:545766238 ecl:hzl
    eyr:2022

    iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
    """
    arr = parse_data(data)
    s2 = solution_2(arr)
    assert s2 == 4
    print("\nSolution 2: {}".format(s2))


def test_solution_2():
    """
    use input.txt
    """
    data = read_input()
    arr = parse_data(data)
    s2 = solution_2(arr)
    assert s2 == 235
    print("\nSolution 1: {}".format(s2))
