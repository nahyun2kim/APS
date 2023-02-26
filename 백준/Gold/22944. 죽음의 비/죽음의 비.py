# boj G4 22944 죽음의 비
# 그래프 # 브루트포스 # 그래프탐색 # BFS # 백트래킹

from collections import deque
import sys
input = sys.stdin.readline

# 상하좌우
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# n: 맵길이, h: 현재 HP, d: 우산 내구도
n, h, d = map(int, input().split())

MAP = []
start = (0, 0)
for i in range(n):
    tmp = list(input())
    if 'S' in tmp:
        start = (i, tmp.index('S'))
    MAP.append(tmp)

visit = [[0]*n for _ in range(n)]

def sol():
    s, e = start
    visit[s][e] = h
    q = deque([(s, e, h, 0, 0)])
    while q:
        st, ed, hp, um, cnt = q.popleft()
        for di, dj in delta:
            nst = st + di
            ned = ed + dj
            if 0 <= nst < n and 0 <= ned < n:
                nhp = hp
                num = um
                if MAP[nst][ned] == 'E':
                    print(cnt + 1)
                    return
                elif MAP[nst][ned] == 'U':
                    num = d - 1
                else:
                    if num > 0:
                        num -= 1
                    else:
                        nhp -= 1
                if nhp == 0:
                    continue
                if visit[nst][ned] < nhp:
                    visit[nst][ned] = nhp
                    q.append((nst, ned, nhp, num, cnt + 1))
    print(-1)

sol()