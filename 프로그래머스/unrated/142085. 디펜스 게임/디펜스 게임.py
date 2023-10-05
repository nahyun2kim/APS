import heapq

def solution(n, k, enemy):
    hq = []
    for i, e in enumerate(enemy):
        heapq.heappush(hq, e)
        if len(hq) > k:
            n -= heapq.heappop(hq)
        if n < 0:
            return i
    return len(enemy)
