from functools import reduce
def solution(n, control):
    dic = {"w": 1, "s": -1, "d": 10, "a": -10}
    for key in control:
        n += dic[key]
    return n