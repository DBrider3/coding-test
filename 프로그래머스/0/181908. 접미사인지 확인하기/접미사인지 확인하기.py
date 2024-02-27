def solution(my_string, is_suffix):
    # version 1
    # return int(my_string[-len(is_suffix):] == is_suffix)
    # version 2
    return int(my_string.endswith(is_suffix))