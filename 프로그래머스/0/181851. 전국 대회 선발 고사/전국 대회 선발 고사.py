def solution(rank, attendance):
    dic = dict(zip(rank, attendance))
    sorted_dic = sorted(dic.items())
    rank_list = []
    for key, value in sorted_dic:
        if value == True:
            rank_list.append(key)
            if len(rank_list) == 3:
                break
    answer = rank.index(rank_list[0]) * 10000 + rank.index(rank_list[1]) * 100 + rank.index(rank_list[2])
    # print(sorted(d.items()))
         
    
         
    return answer