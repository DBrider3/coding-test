def solution(arr):
    answer = 0
    while True:
        arr_tmp = []
        
        for i in arr:
            if i >= 50 and not(i % 2):
                arr_tmp.append(i // 2)
            elif i < 50 and i % 2:
                arr_tmp.append(i * 2 + 1)
            else:
                arr_tmp.append(i)
        if arr == arr_tmp:
            break
        arr = arr_tmp
        answer += 1
    return answer