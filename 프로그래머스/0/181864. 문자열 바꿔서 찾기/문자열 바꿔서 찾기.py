def solution(m, p):
    return 1 if p in ''.join(['B' if i == 'A' else 'A' for i in m]) else 0
    