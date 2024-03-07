
def solution(arr):
    answer = []
    n = len(arr)
    i = 0
    while n > 2 ** i:
        i += 1
    arr.extend([0] * (2 ** i - n))
    return arr