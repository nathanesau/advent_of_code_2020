# Day 2

1. validate passwords. must have char at least ``min`` times 
at most ``max`` times.

2. validate passwords. must have char at in either
position 1 or position 2.

```python
# part 1
# ex. arr = [{"min": 1, "max": 3, "char": "a", "pwd": "abcde"},
#            {"min": 1, "max": 3, "char": "b", "pwd": "cdefg"},
#            {"min": 2, "max": 9, "char": "c", "pwd": "ccccccccc"}]
def solution_1(arr):
    pass_count = 0 
    for p in arr:
        pmin, pmax, pchar, ppwd = p["min"], p["max"], p["char"], p["pwd"]
        count = ppwd.count(pchar)
        if count >= pmin and count <= pmax:
            pass_count += 1
    return pass_count

# part 2
# ex. arr = [{"p1": 0, "p2": 2, "char": "a", "pwd": "abcde"},
#            {"p1": 0, "p2": 2, "char": "b", "pwd": "cdefg"},
#            {"p1": 1, "p2": 8, "char": "c", "pwd": "ccccccccc"}]
def solution_2(arr):
    pass_count = 0
    for p in arr:
        pp1, pp2, pchar, ppwd = p["min"], p["max"], p["char"], p["pwd"]
        if int(ppwd[pp1] == pchar) + int(ppwd[pp2] == pchar) == 1:
            pass_count += 1
    return pass_count
```