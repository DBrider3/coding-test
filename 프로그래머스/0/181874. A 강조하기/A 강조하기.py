def solution(myString):
    return ''.join(["A" if i == 'a' else i for i in myString.lower()])