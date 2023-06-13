import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input().rstrip()))


    def dfs(x, y):
        delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == '#' and not visit[nx][ny]:
                visit[nx][ny] = 1
                dfs(nx, ny)


    visit = [[0]*w for _ in range(h)]
    st = []
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visit[i][j] and grid[i][j] == '#':
                cnt += 1
                dfs(i, j)

    print(cnt)