import os


def solution_1(arr):
    valid_count = 0
    for p in arr:
        pmin, pmax, pchar, ppwd = p["min"], p["max"], p["char"], p["pwd"]
        pchar_count = 0
        for c in ppwd:
            if c == pchar:
                pchar_count += 1
        if pchar_count >= pmin and pchar_count <= pmax:
            valid_count += 1
    return valid_count


def solution_2(arr):
    valid_count = 0
    for p in arr:
        pp1, pp2, pchar, ppwd = p["p1"], p["p2"], p["char"], p["pwd"]
        pchar_count = int(ppwd[pp1] == pchar) + int(ppwd[pp2] == pchar)
        if pchar_count == 1:
            valid_count += 1
    return valid_count
