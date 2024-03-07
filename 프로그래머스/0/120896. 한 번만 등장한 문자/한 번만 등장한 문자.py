def solution(s):
    s = ''.join(sorted(s))
    answer = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    return answer