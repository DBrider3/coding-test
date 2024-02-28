def solution(m, p):
    answer = ''
    for s, e in zip(m, p):
        print(s, e)
        answer += s[e[0]:e[1] + 1]
    
    return answer