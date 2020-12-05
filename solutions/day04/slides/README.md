# Day 4

1. Validate passports. Must have following fields:
    byr, iyr, eyr, hgt, hcl, ecl, pid

2. Validate passports. Must have following fields:
    byr, iyr, eyr, hgt, hcl, ecl, pid

   with additional criteria:
    byr is 4 digit number between 1920 and 2002
    iyr is 4 digit number between 2010 and 2020
    eyr is 4 digit number between 2020 and 2030
    hgt is 3 digits end in 'cm' or 2 digits end in 'in'
    hcl is '#' followed by 6 digit hexadecimal
    ecl is one of 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
    pid is 9 digit number, may have trailing zeros

```python
# data = """
#           ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
#           byr:1937 iyr:2017 cid:147 hgt:183cm
#
#           iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
#           hcl:#cfa07d byr:1929"""
def get_fields(passport):
    fields = []
    for line in passport:
        fields = fields + line.split(' ')
    return fields

def parse_data(arr) -> list: # [["ecl:gry", "pid:123", ...], ["iyr:2013", "ecl:amb", ...]]
    arr = []
    passport = []
    for line in data.splitlines():
        line = line.strip()
        if line:
            passport.append(line)
        else:
            if passport:
                arr.append(get_fields(passport))
            passport = []
    if passport:
        arr.append(get_fields(passport))
    return arr

def solution_1(arr):
    valid_count = 0 
    req_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for passport in arr:
        passport_keys = set()
        for field in passport:
            key, value = field.split(":")
            passports_key.append(key)
        if not req_keys.difference(passports_keys): # empty
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
            return True if v.endswith('cm') and int(v[0:3]) >= 150 and int(v[0:3]) <= 193 \
                else v.endswith('in') and int(v[0:2]) >= 59 and int(v[0:2]) <= 76
        elif k == 'hcl':
            return v[0] == '#' and len(v) == 7 and int(v[1:], 16) >= 0
        elif k == 'ecl':
            return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif k == 'pid':
            return len(v) and int(v) >= 0
        else:
            return True
    except:
        return False

def solution_2(arr):
    valid_count = 0 
    req_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for passport in arr:
        passport_dict = {}
        for field in passport:
            key, value = field.split(":")
            passports_dict[key] = value
        if not req_keys.difference(passports_keys.keys()): # empty
            valid = True
            for k, v in passport_dict.items():
                if not valid_pair(k, v):
                    valid = False
                    break
            if valid:
                valid_count += 1
    return valid_count
```