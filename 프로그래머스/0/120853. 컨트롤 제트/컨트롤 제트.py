def solution(s):
    answer = []
    for i in s.split():
        if i == 'Z':
            if answer:
                answer.pop()
        else:
            answer.append(int(i))
    return sum(answer)
