def solution(board, k):
    answer = 0
    for i, i_value in enumerate(board):
        for j, j_value in enumerate(i_value):
            if i + j <= k:
                answer += board[i][j]  
    return answer 
    # return sum([j for i in board for j in i if j <= k])