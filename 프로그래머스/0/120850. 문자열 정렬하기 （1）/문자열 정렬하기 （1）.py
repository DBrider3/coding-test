def solution(my_string):
    return sorted(map(int, [i for i in my_string if i.isdigit()]))