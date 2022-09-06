N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    temp = input()
    for j in range(N):
        arr[i].append(int(temp[j]))

check = [[0]*N for _ in range(N)]
delta = [[-1, 0], [1,0], [0, -1], [0, 1]]
res = []

def dfs(i,j):
    cnt = 0
    stack = []
    if check[i][j] == 0 and arr[i][j] == 1:
        cnt = 1
        check[i][j] = 1
        stack.append((i,j))
    while stack:
        r, c = stack.pop()
        for k in range(4):
            dr = r + delta[k][0]
            dc = c + delta[k][1]
            if 0 <= dr < N and 0<= dc < N and check[dr][dc] == 0 and arr[dr][dc] == 1:
                cnt += 1
                stack.append((dr, dc))
                check[dr][dc] = 1
                
    return cnt

for i in range(N):
    for j in range(N):
        cnt1 = dfs(i, j)
        if cnt1 > 0:
            res.append(cnt1)
            
            
print(len(res))
res.sort()
for i in range(len(res)):
    print(res[i])