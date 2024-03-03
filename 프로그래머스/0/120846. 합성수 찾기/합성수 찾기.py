def solution(n):
    answer = 0
    for i in range(4, n + 1):
        tmp = 0
        for j in range(1, n + 1):
            if not i % j:
                tmp += 1
            if tmp == 3:
                answer += 1
                break
            
    return answer