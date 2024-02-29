def solution(n_str):
    for i, s in enumerate(n_str):
        print(type(s))
        if s != '0':
            return n_str[i:]