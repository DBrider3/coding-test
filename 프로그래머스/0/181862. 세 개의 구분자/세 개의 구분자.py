def solution(myStr):
    return ''.join([i if i not in ['a','b','c'] else ' ' for i in myStr]).split()
