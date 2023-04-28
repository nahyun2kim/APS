import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # n: 건물의 개수, k: 건물 순서 규칙의 개수
    n, k = map(int, input().split())
    # 각 건물 건축에 걸리는 시간
    times = [0] + list(map(int, input().split()))
    indegree = [0] * (n + 1)
    edges = [[] for _ in range(n + 1)] # 이어지는 규칙
    for _ in range(k):
        x, y = map(int, input().split())
        edges[x].append(y)
        indegree[y] += 1

    h = []
    total = [0] * (n+1)
    for i in range(1, n+1):
        if indegree[i] == 0:
            total[i] = times[i]
            heapq.heappush(h, (total[i], 0, i))

    while h:
        time, pre, now = heapq.heappop(h)
        for right in edges[now]:
            indegree[right] -= 1
            total[right] = max(total[right], time + times[right])
            if indegree[right] == 0:
                 heapq.heappush(h, (total[right], now, right))

    w = int(input())
    print(total[w])