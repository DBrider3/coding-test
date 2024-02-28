def solution(m, p):
    m = list(m)
    for i, v in enumerate(m):
        if v == 'A':
            m[i] = 'B'
        elif v == 'B':
            m[i] = 'A'
    return 1 if p in ''.join(m) else 0