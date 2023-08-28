import heapq as hq

def solution(n, works):
    w = []
    for work in works:
        hq.heappush(w, (-1)*work)
    while w and n > 0:
        now = hq.heappop(w)
        n -= 1
        now += 1
        if now != 0:
            hq.heappush(w, now)
    return sum([i**2 for i in w])