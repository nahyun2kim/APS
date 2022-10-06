import heapq
import sys
input = sys.stdin.readline

N = int(input())
cost = []
for i in range(N):
    cost.append(int(input()))

edges = []
for _ in range(N):
    edges.append(list(map(int, input().split())))

visit = [False]*N
q = []
ans = 0

for i in range(N):
    heapq.heappush(q,(cost[i], i))

while q:
    now = heapq.heappop(q)
    if visit[now[1]]:
        continue
    
    visit[now[1]] = True
    ans += now[0]
    
    for i in range(N):
        if visit[i]:
            continue
        
        heapq.heappush(q,(edges[i][now[1]], i))

print(ans)