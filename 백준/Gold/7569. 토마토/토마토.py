from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

def isripe():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    return False
    return True

def bfs():
    day = 0
    dq = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    dq.append((i, j, k, day))
    
    delta = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]
    while dq:
        i, j, k, day = dq.popleft()
        for d in range(6):
            di = i + delta[d][0]
            dj = j + delta[d][1]
            dk = k + delta[d][2]
            if 0<=di<H and 0<=dj<N and 0<=dk<M and tomato[di][dj][dk] == 0:
                dq.append((di, dj, dk, day+1))
                tomato[di][dj][dk] = 1
    
    if isripe():
        return day
    else:
        return -1
        
tomato = []
for _ in range(H):
    floor = []
    for _ in range(N):
        floor.append(list(map(int,input().split())))
    tomato.append(floor)
    
if isripe():
    print(0)
else:
    day = bfs()
    print(day)
