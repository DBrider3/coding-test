def solution(a, b):
    if a % 2 and b % 2:
        return a ** 2 + b ** 2
    elif a % 2 or b % 2:
        return (a + b) * 2
    else:
        return abs(a - b)
    