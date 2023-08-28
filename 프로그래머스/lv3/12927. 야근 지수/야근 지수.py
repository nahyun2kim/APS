import heapq as hq

def solution(n, works):
    answer = 0
    w = []
    for work in works:
        hq.heappush(w, (-1)*work)
    while w and n > 0:
        now = hq.heappop(w)
        n -= 1
        now += 1
        if now != 0:
            hq.heappush(w, now)
    for w in w:
        answer += w**2
    return answer