from heapq import heappush, heappop

def solution(N, road, K):
    answer = 0
    roads = [[] for _ in range(N+1)]
    distance = [987654321] * (N+1)
    for a, b, c in road:
        roads[a].append((b, c))
        roads[b].append((a, c))
    
    def dijkstra(start):
        q = []
        heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heappop(q)
            if distance[now] < dist:
                continue
            for n, c in roads[now]:
                cost = dist + c
                if cost < distance[n]:
                    distance[n] = cost
                    heappush(q, (cost, n))
    dijkstra(1)
    for d in range(1, N+1):
        if distance[d] <= K:
            answer += 1
    return answer