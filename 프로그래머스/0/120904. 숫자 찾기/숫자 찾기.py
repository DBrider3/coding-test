def solution(num, k):
    # version 1
    # try:
    #     return str(num).index(str(k)) + 1
    # except:
    #     return -1
    # version 2
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1