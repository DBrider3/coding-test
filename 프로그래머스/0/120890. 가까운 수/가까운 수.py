def solution(array, n):
    answer = []
    m = abs(array[0] - n)
    for numb in array:
        if m > abs(numb - n):
            m = abs(numb - n)
            answer = [numb]
        elif m == abs(numb - n):
            answer.append(numb)
    return min(answer)