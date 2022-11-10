from collections import deque

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 동남서북 (시계방향)
n = int(input())
k = int(input())
ground = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    ground[x-1][y-1] = 2
l = int(input())
info = {}
for _ in range(l):
    x, c = input().split()
    info[int(x)] = c

time = 0
x = 0
y = 0
ground[x][y] = 1
pos = deque([[0, 0]])
d = 0
while True:
    time += 1
    nx = x + delta[d][0]
    ny = y + delta[d][1]
    if 0 <= nx < n and 0 <= ny < n:
        if ground[nx][ny] == 0:
            i, j = pos.popleft()
            ground[i][j] = 0
        elif ground[nx][ny] == 1:
            break
        ground[nx][ny] = 1
        pos.append([nx, ny])
        x = nx
        y = ny
    else:
        break

    if time in info.keys():
        if info[time] == 'L':
            d = (d-1) % 4
        else:
            d = (d+1) % 4

print(time)