def solution(my_string):
    # version 1
    # answer = ''
    # for i in my_string:
    #     if i not in answer:
    #         answer += i
    # return answer
    # version 2
    return ''.join(dict.fromkeys(my_string))