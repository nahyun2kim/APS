import sys
input = sys.stdin.readline
INF = int(1e9)

# 마을 개수 V, 도로 개수 E
V, E = map(int, input().split(' '))

road = [[INF for _ in range(V + 1)] for _ in range(V + 1)]

# 도로 정보 (출발, 도착, 거리)
for _ in range(E):
  a, b, c = map(int, input().split(' '))
  road[a][b] = c

for i in range(1, V + 1):
  for j in range(1, V + 1):
    for k in range(1, V + 1):
      road[i][j] = min(road[i][j], road[i][k] + road[k][j])

answer = INF
for i in range(1, V + 1):
  answer = min(answer, road[i][i])

print(answer if answer != INF else -1)