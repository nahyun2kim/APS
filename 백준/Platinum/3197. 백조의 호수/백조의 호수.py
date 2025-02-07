from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 백조가 만날수 있는지 체크
def isMeet(maps, visit, q, swan):
  r, c = len(maps), len(maps[0])
  next_q = deque()
  while q:
    x, y = q.popleft()
    if x == swan[1][0] and y == swan[1][1]:
      return True, None

    for dx, dy in delta:
      nx = x + dx
      ny = y + dy
      if not 0 <= nx < r or not 0 <= ny < c or visit[nx][ny]:
        continue
      if maps[nx][ny] == 'X':
        next_q.append((nx, ny))
      else:
        q.append((nx, ny))
      visit[nx][ny] = 1

  return False, next_q

# 물과 맞닿은 빙판이 녹음
def melt(maps, q):
  r, c = len(maps), len(maps[0])
  next_q = deque()
  while q:
    x, y = q.popleft()
    for dx, dy in delta:
      nx = x + dx
      ny = y + dy
      if not 0 <= nx < r or not 0 <= ny < c:
        continue
      if maps[nx][ny] == 'X':
        next_q.append((nx, ny))
        maps[nx][ny] = '.'
    
  return next_q

# 행 R, 열 C
R, C = map(int, input().split(' '))
maps = []
swan = []
water = deque()

for i in range(R):
  info = list(input().rstrip())
  for j in range(C):
    if info[j] == '.':
      water.append((i, j))
    if info[j] == 'L':
      water.append((i, j))
      swan.append((i, j)) 
  maps.append(info)

day = -1
visited = [[0 for _ in range(C)] for _ in range(R)]
q = deque()

sx, sy = swan[0][0], swan[0][1]
q.append((sx, sy))
visited[sx][sy] = 1

while True:
    day += 1
    found, next_q = isMeet(maps, visited, q, swan)
    if found:
        break
    water = melt(maps, water)
    q = next_q

print(day)
