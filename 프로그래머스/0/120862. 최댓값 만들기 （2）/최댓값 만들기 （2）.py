def solution(numbers):
    max_value = numbers[0] * numbers[1]
    for i, i_value in enumerate(numbers):
        for j, j_value in enumerate(numbers):
            if j > i:
                tmp = i_value * j_value
                if max_value < tmp:
                    max_value = tmp
    return max_value
                