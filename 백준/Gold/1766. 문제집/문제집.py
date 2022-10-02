import heapq
import sys
input = sys.stdin.readline

# N: 문제의 수, M: 문제들의 정보 수
N, M = map(int, input().split())

# 먼제 풀면 좋은 문제들 정보
order = {}
indegree = [0]*(N+1) # 진입차수 리스트
for _ in range(M):
    a, b = map(int, input().split())
    if a in order.keys():
        order[a].append(b)
    else:
        order[a] = [b]
    indegree[b] += 1

# 위상정렬 사용
queue = []
ans = []

# 우선 먼저푸는 문제가 없는 애들부터 push
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    now = heapq.heappop(queue)
    ans.append(now)
    if not now in order.keys():
        continue
    for i in order[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(queue, i)


print(" ".join(map(str,ans)))