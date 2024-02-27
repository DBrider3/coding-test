def solution(arr):
    for i, _ in enumerate(arr):
        if arr[i] >= 50 and not arr[i] % 2:
            arr[i] //= 2
        elif arr[i] < 50 and arr[i] % 2:
            arr[i] *= 2
    return arr