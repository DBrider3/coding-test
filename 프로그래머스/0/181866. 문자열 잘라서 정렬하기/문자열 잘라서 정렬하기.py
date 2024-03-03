def solution(myString):
    a = sorted(myString.split('x'))
    return [i for i in a if i]