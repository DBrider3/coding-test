def solution(arr):
    answer = []
    two_index = []
    for index, value in enumerate(arr):
        if value == 2:
            two_index.append(index)
    if not len(two_index):
        answer.append(-1)
    else:
        answer = arr[two_index[0]:two_index[-1] + 1]
    return answer