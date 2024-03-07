def solution(n):
    answer = 0
    f = 1
    i = 1
    while n > f * i:
        i += 1
        f *= i
    return i