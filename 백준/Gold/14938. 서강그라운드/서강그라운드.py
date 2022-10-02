import sys
input = sys.stdin.readline

# n: 지역의 개수, m: 수색범위, r: 길의 개수
n, m, r = map(int, input().split())

# 아이템들
items = list(map(int, input().split()))

# 간선 정보 입력
edges = [[] for _ in range(n+1)]
for _ in range(r):
    u, w, l = map(int, input().split())
    edges[u].append((w, l))
    edges[w].append((u, l))

INF = sys.maxsize
d = [[INF]*(n+1) for _ in range(n+1)]
visit = [[False]*(n+1) for _ in range(n+1)]

# 방문하지 않은 점 중 최소길이의 인덱스 찾기
def find_small_idx(st):
    mini = INF
    idx = 0
    for i in range(1, n+1):
        if visit[st][i] == False and mini > d[st][i]:
            mini = d[st][i]
            idx = i
    return idx

# 다익스트라
def dijkstra(st):
    d[st][st] = 0
    
    for _ in range(n-1):
        now = find_small_idx(st)
        if now == 0:
            break
        visit[st][now] = True
        
        for edge in edges[now]:
            if visit[st][edge[0]] == False and d[st][edge[0]] > d[st][now] + edge[1]:
                d[st][edge[0]] = d[st][now] + edge[1]

for i in range(1, n+1):
    dijkstra(i)
    
max_item = 0
for i in range(1, n+1):
    total = 0
    for j in range(1, n+1):
        if d[i][j] <= m:
            total += items[j-1]
    max_item = max(max_item, total)

print(max_item)