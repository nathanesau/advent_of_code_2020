# Day 1

1. find the two entries in a list that sum to 2020 
and multiply them together.

2. find the product of three entries that sum to 2020.

```python
# part 1
# ex. arr = [1721, 979, 366, 299, 675, 1456]
def solution_1(arr, target=2020):
    m1 = {}
    for num in arr:
        m1[num] = num
    for num in arr:
        if (target-num) in m1:
            return (target-num) * num
    return None

# part 2
# ex. arr = [1721, 979, 366, 299, 675, 1456]
def solution_2(arr, target=2020):
    m2 = {}l
    for num1 in arr:
        for num2 in arr:
            m2[num1+num2] = num1*num2
    for num in arr:
        if (target-num) in m2:
            return m2[target-num] * num
    return None
```