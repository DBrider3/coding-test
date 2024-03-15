def is_digit(s):
    try:
        tmp = int(s)
        return True
    except ValueError:
        return False

def solution(s):
    answer = 0
    splitS = s.split(' ')
    tmp = 0
    for i in splitS:
        if is_digit(i):
            tmp = int(i)
            answer += tmp
        else:
            answer -= tmp
        
    return answer