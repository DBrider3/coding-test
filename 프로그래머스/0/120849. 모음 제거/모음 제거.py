def solution(my_string):
    string_list = list(my_string)
    mo = ["a","e","i","o","u"]
    for i, value in enumerate(string_list):
        if value in mo:
            string_list[i] = ''
    # my_string.replace()
    return "".join(string_list)