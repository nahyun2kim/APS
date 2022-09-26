#import sys
#input = sys.stdin.readline

delta = [[-1,0],[1,0],[0,-1],[0,1]]

def wire():
    tmp = []
    for i in range(N):
        tmp.append(processor[i].copy())
    cnt = 0
    length = 0
    for i in range(C):
        if sel[i] <0:
            continue
        if not check(core[i][0], core[i][1], sel[i], tmp):
            continue
        cnt += 1
        di = core[i][0] + delta[sel[i]][0]
        dj = core[i][1] + delta[sel[i]][1]
        while 0<=di<N and 0<=dj<N:
            tmp[di][dj] = 1
            length += 1
            di += delta[sel[i]][0]
            dj += delta[sel[i]][1]
    return cnt, length

def perm(idx):
    global max_cnt, min_len
    
    if idx == C:
        cnt, length = wire()
        if cnt > max_cnt:
            max_cnt = cnt
            min_len = length
        elif cnt == max_cnt:
            min_len = min(min_len, length)
        return
    flag = False
    for d in range(4):
        
        if check(core[idx][0], core[idx][1], d, processor):
            flag = True
            sel[idx] = d
            perm(idx+1)
    if not flag:
        sel[idx] = -1
        perm(idx+1)
        
def check(i, j, d, arr):
    di = i+delta[d][0]
    dj = j+delta[d][1]
    while 0<=di<N and 0<=dj<N:
        if arr[di][dj] == 1:
            return False
        di += delta[d][0]
        dj += delta[d][1]
    return True
    
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    processor = []
    core = []
    for _ in range(N):
        processor.append(list(map(int, input().split())))
    for i in range(1,N-1):
        for j in range(1,N-1):
            if processor[i][j] == 1:
                core.append([i, j])
    
    C = len(core)
    sel = [0]*C
    max_cnt = 0
    min_len = N*N
    
    perm(0)
    
    print('#{} {}'.format(tc, min_len))
    
