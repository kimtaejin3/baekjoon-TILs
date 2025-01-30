def f(rank):
    if rank == 6:
        return 1
    elif rank == 5:
        return 2
    elif rank == 4:
        return 3
    elif rank == 3:
        return 4
    elif rank == 2:
        return 5
    else:
        return 6
    
def solution(lottos, win_nums):
    # 최고 순위의 경우: 0이 다 맞았을때
    # 최저 순위의 경우: 0이 다 틀렸을때
    
    count_unknowns = 0
    count_equals = 0
        
    for lotto in lottos:
        if lotto == 0:
            count_unknowns += 1
    
    for lotto in lottos:
        if lotto in win_nums:
            count_equals += 1
    
    high_ranking = count_equals + count_unknowns
    low_ranking = count_equals
    
    
    return [f(high_ranking), f(low_ranking)]