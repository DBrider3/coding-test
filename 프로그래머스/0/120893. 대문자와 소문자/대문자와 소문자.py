def solution(my_string):
    # version 1
    # return ''.join([s.lower() if s.isupper() else s.upper() for s in my_string])
    # version 2
    return my_string.swapcase()