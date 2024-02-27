from functools import reduce

def solution(num_list):
    return reduce(lambda x, y: x + y, num_list) if len(num_list) > 10 else reduce(lambda x, y: x * y, num_list)