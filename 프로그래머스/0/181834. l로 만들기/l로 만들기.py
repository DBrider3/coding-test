def solution(myString):
    myString = list(myString)
    for i, s in enumerate(myString):
        if s < 'l':
            myString[i] = 'l'
    return ''.join(myString)