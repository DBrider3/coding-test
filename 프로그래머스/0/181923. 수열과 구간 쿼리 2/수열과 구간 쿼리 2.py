def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        tmp = []
        limit_arr = arr[s:e+1]
        for i in limit_arr:
            if k < i:
                tmp.append(i)
        if tmp:
            answer.append(min(tmp))
        else:
            answer.append(-1)
    return answer