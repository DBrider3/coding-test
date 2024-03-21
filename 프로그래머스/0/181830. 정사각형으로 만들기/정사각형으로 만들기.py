def solution(arr):
    len_total = len(arr)
    len_one = len(arr[0])
    if len_total > len_one:
        gap = len_total - len_one
        for index, _ in enumerate(arr):
            arr[index].extend([0] * gap)
    elif len_one > len_total:
        gap = len_one - len_total
        for i in range(gap):
            arr.append([0] * len_one)
    return arr