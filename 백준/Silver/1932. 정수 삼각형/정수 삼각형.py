import sys
input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

path = [[0]*(i+1) for i in range(N)]

path[0][0] = triangle[0][0]
for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            path[i][j] = path[i-1][j] + triangle[i][j]
        elif j == i:
            path[i][j] = path[i-1][j-1] + triangle[i][j]
        else:
            path[i][j] = max(path[i-1][j-1], path[i-1][j]) + triangle[i][j]

print(max(path[N-1]))