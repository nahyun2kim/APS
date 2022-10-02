import heapq
import sys
input = sys.stdin.readline

# N: 가수의 수, M: 보조피디의 수
N, M = map(int, input().split())

# 피디들이 정한 순서 모집,,
indegree = [0]*(N+1)
order = {}
for _ in range(M):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        if tmp[i] in order.keys():
            order[tmp[i]].append(tmp[i+1])
        else:
            order[tmp[i]] = [tmp[i+1]]
        indegree[tmp[i+1]] += 1

visit = [False]*(N+1)
queue = []
ans = []

# 진입차수가 0인 애들부터 push
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)

# 큐에서 꺼내가며 담에 누가할 지 비교
while queue:
    now = heapq.heappop(queue)
    visit[now] = True
    ans.append(now)
    
    if not now in order.keys():
        continue
    
    for i in order[now]:
        indegree[i] -= 1
        if indegree[i] == 0 and visit[i] == False:
            heapq.heappush(queue, i)

if len(ans) == N:
    for i in ans:
        print(i)
else:
    print(0)