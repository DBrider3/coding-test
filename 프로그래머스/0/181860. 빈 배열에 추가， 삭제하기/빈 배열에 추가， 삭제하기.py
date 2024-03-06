def solution(arr, flag):
    answer = []
    for i, f in enumerate(flag):
        for j in range(arr[i]):
            if f:
                for k in range(2):
                    answer.append(arr[i])
            else:
                answer.pop()
    return answer