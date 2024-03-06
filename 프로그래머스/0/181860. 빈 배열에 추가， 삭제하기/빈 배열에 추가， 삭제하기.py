def solution(arr, flag):
    ans = []
    for i, f in zip(arr, flag):
        if f:
            ans += [i] * i * 2
        else:
            ans = ans[:-i]
    return ans