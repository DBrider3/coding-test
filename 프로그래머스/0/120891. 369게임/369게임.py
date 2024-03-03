def solution(order):
    game = ["3", "6", "9"]
    answer = 0
    for i in str(order) :
        if i in game:
            answer += 1
    
    return answer