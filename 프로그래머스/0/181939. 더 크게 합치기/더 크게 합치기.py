def solution(a, b):
    return max(int(''.join(str(a) + str(b))), int(''.join(str(b) + str(a))))