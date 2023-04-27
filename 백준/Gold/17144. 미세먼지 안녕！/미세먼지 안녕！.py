import sys
input = sys.stdin.readline

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우

r, c, t = map(int, input().split())
total = 0 # 총 먼지의 양
dust = [] # 미세 먼지 배열
fresh = []
for i in range(r):
    tmp = list(map(int, input().split()))
    dust.append(tmp)
    if -1 in tmp:
        total += sum(tmp) + 1
        fresh.append((i, tmp.index(-1)))
    else:
        total += sum(tmp)


# 사방향 확산
def diffusion(i, j, new_dust):
    diff = dust[i][j] // 5
    for di, dj in delta:
        ii = i + di
        jj = j + dj
        if 0 <= ii < r and 0 <= jj < c and dust[ii][jj] != -1:
            new_dust[ii][jj] += diff
            new_dust[i][j] -= diff


# 순환
def move(i, j, new_dust):
    global total
    # 같은 행이면 --> 오른쪽 이동
    if (i == fresh[0][0] or i == fresh[1][0]) and j < c-1:
        new_dust[i][j+1] = dust[i][j]
    # 위로 순환
    elif (0 < i <= fresh[0][0] and j == c - 1) or (fresh[1][0] + 1 < i < r and j == 0):
        new_dust[i-1][j] = dust[i][j]
    # 아래로 순환
    elif (0 <= i < fresh[0][0] -1 and j == 0) or (fresh[1][0] <= i < r-1 and j == c - 1):
        new_dust[i+1][j] = dust[i][j]
    # 왼쪽으로 순환
    elif (i == 0 or i == r -1) and j > 0:
        new_dust[i][j-1] = dust[i][j]
    # 공기청정기로 빨려들어감
    elif (i == fresh[0][0] -1 or i == fresh[1][0] + 1) and j == 0:
        total -= dust[i][j]
    else:
        new_dust[i][j] = dust[i][j]

for x in range(t):
    new_dust = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if dust[i][j] != -1 and dust[i][j] != 0:
                new_dust[i][j] += dust[i][j]
                diffusion(i, j, new_dust)
            elif dust[i][j] == -1:
                new_dust[i][j] = -1
    # 확산이 끝난 후 갈아 끼우기
    dust = [n[:] for n in new_dust]
    new_dust = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not dust[i][j] == -1:
                move(i, j, new_dust)
            else:
                new_dust[i][j] = -1

    # 이동이 끝난 후 갈아 끼우기
    dust = [n[:] for n in new_dust]

print(total)