def solution(my_string, is_suffix):
    return 1 if len(my_string) >= len(is_suffix) and my_string[-len(is_suffix):] == is_suffix else 0