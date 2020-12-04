def solution_1(arr):
    req_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    opt_keys = {"cid"}
    valid_count = 0
    for passport in arr:
        passport_keys = set()
        for field in passport:
            key, value = field.split(":")
            passport_keys.add(key)
        if not req_keys.difference(passport_keys):
            valid_count += 1
    return valid_count


def valid_pair(k, v):
    try:
        if k == 'byr':
            return int(v) >= 1920 and int(v) <= 2002
        elif k == 'iyr':
            return int(v) >= 2010 and int(v) <= 2020
        elif k == 'eyr':
            return int(v) >= 2020 and int(v) <= 2030
        elif k == 'hgt':
            return (
                True if v.endswith('cm') and int(v[0:3]) >= 150 and int(v[0:3]) <= 193
                else v.endswith('in') and int(v[0:2]) >= 59 and int(v[0:2]) <= 76)
        elif k == 'hcl':
            return v[0] == '#' and len(v) == 7 and int(v[1:], 16) >= 0
        elif k == 'ecl':
            return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif k == 'pid':
            return len(v) == 9 and int(v) >= 0 
        else:
            return True
    except:
        return False


def solution_2(arr):
    req_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    opt_keys = {"cid"}
    valid_count = 0
    for passport in arr:
        passport_dict = {}
        for field in passport:
            key, value = field.split(":")
            passport_dict[key] = value
        if not req_keys.difference(set(passport_dict.keys())):
            valid = True
            for k, v in passport_dict.items():
                if not valid_pair(k, v):
                    valid = False
                    break
            if valid:
                valid_count += 1
    return valid_count
