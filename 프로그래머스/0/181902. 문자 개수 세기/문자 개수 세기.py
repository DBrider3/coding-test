import string

def solution(my_string):
    answer = []
    all_case = dict.fromkeys(string.ascii_uppercase, 0)   
    lower_case = dict.fromkeys(string.ascii_lowercase, 0)   
    all_case.update(lower_case)
    
    for i in my_string:
        all_case[i] += 1
    
    return list(all_case.values())