import sys
input = sys.stdin.readline

# n: 세로, m: 가로
n, m = map(int, input().split())

# 숫자들
nums = []
max_num = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    max_num = max(max_num, max(tmp))
    nums.append(tmp)

# 상하좌우
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 방문체크용
visit = [[False]*m for _ in range(n)]

ans = 0


def dfs(x, y, cnt, total):
    global ans
    if cnt == 4:
        ans = max(ans, total)
        return
    if cnt == 3 and total + max_num <= ans:
        return

    for d in range(4):
        nx = x + delta[d][0]
        ny = y + delta[d][1]
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            # ㅗ 모양을 만들기 위한 작업
            if cnt == 2:
                visit[nx][ny] = True
                dfs(x, y, cnt + 1, total + nums[nx][ny])
                visit[nx][ny] = False

            visit[nx][ny] = True
            dfs(nx, ny, cnt + 1, total + nums[nx][ny])
            visit[nx][ny] = False


for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i, j, 1, nums[i][j])
        visit[i][j] = False

print(ans)