def solution(my_string):
    test = ''.join([i_value if i_value.isdigit() else ' ' for i_value in my_string]).split(' ')
    c = sum(map(lambda x: int(x) if x.isdigit() else 0, test))
    return c