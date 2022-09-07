import sys
import math
input = sys.stdin.readline


N, L, R = map(int, input().split())
peo = []
for _ in range(N):
    peo.append(list(map(int, input().split())))

    

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def move_peo(r, c):
    stack = []
    stack.append((r,c))
    check[r][c] = 1
    res = []
    while stack:
        i,j = stack.pop()
        res.append((i,j))
        for d in range(4):
            di = i + delta[d][0]
            dj = j + delta[d][1]
            if 0<=di<N and 0<=dj<N and check[di][dj] == 0 and L<=abs(peo[i][j]-peo[di][dj])<=R:
                check[di][dj] = 1
                stack.append((di,dj))
    return res
        
    

count = 0
while True:
    move =[]
    flag = 0
    check = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res = move_peo(i,j)
            if not len(res) == 1:
                move.append(res)
    
    if len(move) == 0:
        break
    else:
        count += 1
        for i in range(len(move)):
            sum_peo = 0
            for ii, jj in move[i]:
                sum_peo += peo[ii][jj]
            new = math.floor(sum_peo/len(move[i]))
            for ii, jj in move[i]:
                peo[ii][jj] = new

print(count)