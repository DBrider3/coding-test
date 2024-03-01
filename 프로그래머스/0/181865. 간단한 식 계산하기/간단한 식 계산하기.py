def solution(b):
    op = ['+', '-', '*']
    b = b.split(' ')

    if b[1] == op[0]:
        answer = int(b[0]) + int(b[2])
    elif b[1] == op[1]:
        answer = int(b[0]) - int(b[2])
    else:
        answer = int(b[0]) * int(b[2])
    return answer