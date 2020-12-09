def solution_1(arr, preamble):
    m2 = {} # count of each pair-sum
    for i in range(preamble):
        for j in range(1, preamble, 1):
            if arr[i] + arr[j] not in m2:
                m2[arr[i] + arr[j]] = 1
            else:
                m2[arr[i] + arr[j]] += 1
    for i, num in enumerate(arr[preamble:]):
        if num not in m2:
            return num
        # decrease pair-sum count for arr[index]
        num_index = arr[i]
        for j in range(i+1, i+preamble, 1):
            # num_index+arr[j] will be in m2
            m2[num_index+arr[j]] = m2[num_index+arr[j]] - 1
            if m2[num_index+arr[j]] <= 0:
                del m2[num_index+arr[j]]
        # increase pair-sum count for arr[preamble+index]
        for j in range(i+1, i+preamble, 1):
            if num + arr[j] not in m2:
                m2[num+arr[j]] = 1
            else:
                m2[num+arr[j]] += 1
    return None


def solution_2(arr, target):
    prev_dict = dict(((i, i), num) for i, num in enumerate(arr))
    curr_dict = {}
    for n in range(2, len(arr)):
        for i in range(0, len(arr) - n):
            curr_value = prev_dict[(i, i+n-2)] + arr[i+n-1]
            curr_dict[(i, i+n-1)] = curr_value
            if curr_value == target:
                return min(arr[i:(i+n)]) + max(arr[i:(i+n)])
        prev_dict = curr_dict
    return None
