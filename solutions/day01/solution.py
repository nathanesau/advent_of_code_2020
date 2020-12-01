import os


def solution_1(arr, target=2020):
    """
    - find the two entries that sum to target
    - what do you get if you multiply them together?
    """
    m1 = {}
    for num in arr:
        m1[num] = num

    for num in arr:
        if (target - num) in m1:
            return m1[target - num] * num

    return None


def solution_2(arr, target=2020):
    """
    - find the three entries that sum to target
    - what do you get if you multiply them together?
    """
    m2 = {}
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            m2[arr[i]+arr[j]] = arr[i]*arr[j]

    for num in arr:
        if (target - num) in m2:
            return m2[target - num] * num

    return None
