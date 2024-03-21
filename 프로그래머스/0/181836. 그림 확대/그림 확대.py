def solution(picture, k):
    answer = []
    

    for p in picture:
        tmp = ''
        for s in p:
            tmp += (s * k)
        for i in range(k):
            answer.append(tmp)
    return answer