def solution(k, dungeons):
    max_ans = 0
    visit = [False]*len(dungeons)
    def tour(idx, hp, cnt):
        nonlocal max_ans
        
        if idx == len(dungeons):
            max_ans = max(max_ans, cnt)
            return
        
        for i in range(len(dungeons)):
            if not visit[i]:
                visit[i] = True
                if hp >= dungeons[i][0]:
                    tour(idx+1, hp-dungeons[i][1], cnt+1)
                else:
                    tour(idx+1, hp, cnt)
                visit[i] = False
                
    tour(0, k, 0)
    answer = max_ans
    return answer