def solution(N, stages):
    stage_cnt = [0]*(N+1)
    clear = 0
    for i in stages:
        if i == N+1:
            clear += 1
            continue
        stage_cnt[i] += 1
        
    member = [0]*N + [stage_cnt[N]]
    for i in range(N-1,0,-1):
        member[i] = member[i+1] + stage_cnt[i]
    
    fail = []
    for i in range(1, N+1):
        if member[i] + clear == 0:
            failure_rate = 0
        else:
            failure_rate = stage_cnt[i] / (member[i] + clear)
        fail.append((i, failure_rate))
        
    fail.sort(key = lambda x : -x[1])
    answer = [x[0] for x in fail]
    return answer