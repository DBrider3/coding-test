def solution(A, B):
    if A == B:
        return 0
    
    answer = 0
    for j in range(len(A)):
        tmp = list(A)
        for i in range(len(A)):
            tmp[(i + 1) % len(A)] = A[i]
        A = ''.join(tmp)
        answer += 1
        if A == B:
            break
    
    return answer if answer != len(A) else -1 