def solution(spell, dic):
    answer = 2
    for d in dic:
        tmp = 0
        for s in spell:
            if s in d:
                tmp += 1
        if tmp == len(spell):
            return 1
    return answer