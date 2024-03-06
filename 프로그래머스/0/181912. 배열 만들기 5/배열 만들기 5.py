def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        tmp = int(intStr[s:s+l])
        if k < tmp:
            answer.append(tmp)
        
        
    return answer