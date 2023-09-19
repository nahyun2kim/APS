def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    same = zero = 0
    for lotto in lottos:
        if lotto == 0: 
            zero += 1
        elif lotto in win_nums:
            same += 1
    return [rank[same+zero], rank[same]]