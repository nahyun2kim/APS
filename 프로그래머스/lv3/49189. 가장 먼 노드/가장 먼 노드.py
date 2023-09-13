import heapq as hq

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for st, ed in edge:
        graph[st].append(ed)
        graph[ed].append(st)
    dist = [123456789] * (n + 1)
    q = []
    hq.heappush(q, (0, 1))
    while q:
        cnt, now = hq.heappop(q)
        if cnt > dist[now]: continue
        for i in graph[now]:
            if cnt + 1 < dist[i]:
                dist[i] = cnt + 1
                hq.heappush(q, (cnt + 1, i))
    val = max(dist[2:])
    return dist[2:].count(val)