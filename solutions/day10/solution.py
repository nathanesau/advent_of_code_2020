def solution_1(arr):
    arr = sorted(arr)
    prev_adapter = 0
    count = {1:0, 3:0}
    for adapter in arr:
        diff = adapter - prev_adapter
        count[diff] += 1
        prev_adapter = adapter
    count[3] += 1 # last item
    return count[1] * count[3]


def solution_2(arr):
    arr = sorted(arr)
    partial = [0 for i in range(len(arr))]
    partial[0] = 1
    for i in range(1, len(arr)):
        count = 0
        j = i - 1
        while j >= 0 and arr[i] - arr[j] <= 3:
            count += partial[j] # all paths before and including arr[j]
            j -= 1
        partial[i] = count
    return partial[-1]
