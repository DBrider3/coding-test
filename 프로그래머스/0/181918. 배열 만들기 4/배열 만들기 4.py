def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not len(stk): # 빈 배열일 경우
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]: # 원소가 있고 마지막원소가 더 작을때
            stk.append(arr[i])
            i += 1
        else: # 마지막원소가 더 크거나 같을때
            stk.pop()
            
    return stk