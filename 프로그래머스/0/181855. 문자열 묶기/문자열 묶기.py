def solution(strArr):
    a = [len(s) for s in strArr]
    tmp = []
    for i in set(a):
        tmp.append(a.count(i))
    return max(tmp)