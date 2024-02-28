def solution(hp):
    answer = 0
    a, b = divmod(hp, 5)
    answer += a
    a, b = divmod(b, 3)
    answer += (a + b)
    return answer