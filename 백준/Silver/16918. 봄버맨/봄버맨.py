import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
ground = [list(input()) for _ in range(R)]

delta = [[-1,0],[1,0],[0,-1],[0,1]]

def bomber():
    bomb = []
    global ground
    for i in range(R):
        for j in range(C):
            if ground[i][j] == 'O':
                bomb.append((i,j))
                
    arr = [['O']*C for _ in range(R)]           
    for k in range(len(bomb)):
        i, j = bomb[k]
        arr[i][j] = '.'
        for d in range(4):
            dr = i + delta[d][0]
            dc = j + delta[d][1]
            if 0<=dr<R and 0<=dc<C and arr[dr][dc] == 'O':
                arr[dr][dc] = '.'
    ground = arr     
    return bomb


if N%2 == 0:
    ans = [['O']*C for _ in range(R)]
else:
    for _ in range(N//2):
        bomb = bomber()
    ans = ground
    
for i in range(R):
    for j in range(C):
        print(ans[i][j], end='')
    print()