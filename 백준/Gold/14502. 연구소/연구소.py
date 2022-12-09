from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# n, m: 세로, 가로의 길이
n, m = map(int, input().split())

# 지도 모양
ground = []
for _ in range(n):
    ground.append(list(map(int, input().split())))

# 바이러스와 빈칸의 좌표 저장
virus = []
blanks = []
for i in range(n):
    for j in range(m):
        if ground[i][j] == 2:
            virus.append((i, j))
        elif ground[i][j] == 0:
            blanks.append((i,j))

def count_safe():
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visit = [[False]*m for _ in range(n)]
    for i,j in virus:
        if not visit[i][j]:
            q = deque([(i,j)])
            visit[i][j] = True
            while q:
                ii, jj = q.popleft()
                for d in range(4):
                    di = ii + delta[d][0]
                    dj = jj + delta[d][1]
                    if 0<=di<n and 0<=dj<m and not visit[di][dj] and ground[di][dj] != 1:
                        visit[di][dj] = True
                        q.append((di, dj))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 0 and not visit[i][j]:
                cnt += 1
    return cnt

ans = 0
select = list(combinations(blanks, 3))
for sel in select:
    for i,j in sel:
        ground[i][j] = 1
    ans = max(ans, count_safe())
    for i,j in sel:
        ground[i][j] = 0


print(ans)