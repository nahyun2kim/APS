import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visit = [[-1]*m for _ in range(n)]
delta = [[1, 0], [0, 1], [0, -1], [-1, 0]] # 아래. 오른, 왼, 위


def dfs(i, j):
    if i == n-1 and j == m-1:
        return 1

    if visit[i][j] != -1:
        return visit[i][j]

    visit[i][j] = 0
    for di, dj in delta:
        ni = i + di
        nj = j + dj
        if 0 <= ni < n and 0 <= nj < m and arr[i][j] > arr[ni][nj]:
            visit[i][j] += dfs(ni, nj)

    return visit[i][j]


print(dfs(0, 0))