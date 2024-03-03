def solution(numLog):
    dic = dict(zip([1,-1,10,-10], ["w","s","d","a"]))

    answer = ''
    for i in range(len(numLog) - 1):
        answer += dic[numLog[i + 1] - numLog[i]]
    return answer