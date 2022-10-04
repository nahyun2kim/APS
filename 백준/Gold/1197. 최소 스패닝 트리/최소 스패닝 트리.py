import sys
input = sys.stdin.readline

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())

# 간선들 저장
edges = {}
for _ in range(E):
    a,b,c = map(int, input().split())
    if a in edges.keys():
        edges[a].append((b,c))
    else:
        edges[a] = [(b,c)]
    if b in edges.keys():
        edges[b].append((a,c))
    else:
        edges[b] = [(a,c)]

INF = sys.maxsize    

# 방문처리용
visit = [False]*(V+1)

# 가중치를 저장할 용
dist = [INF]*(V+1)

# 1번을 시작점으로 잡자
dist[1] = 0

ans = 0
for _ in range(V-1):
    mini = INF
    idx = 0
    # 방문 안한 정점 중 가장 작은 값
    for i in range(1, V+1):
        if not visit[i] and dist[i] < mini:
            mini = dist[i]
            idx = i
    
    # 뽑은 idx에 방문처리
    visit[idx] = True
    
    if not idx in edges.keys():
        continue
    
    # 다음 갱신
    for i in edges[idx]:
        if not visit[i[0]] and dist[i[0]] > i[1]:
            dist[i[0]] = i[1]

for i in range(1, V+1):
    ans += dist[i]

print(ans)