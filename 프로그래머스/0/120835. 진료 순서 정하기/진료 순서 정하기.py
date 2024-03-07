def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    for n in emergency:
        answer.append(sorted_emergency.index(n) + 1)
    return answer