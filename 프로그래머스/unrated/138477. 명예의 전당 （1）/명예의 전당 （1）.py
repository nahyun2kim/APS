import heapq as hq
def solution(k, score):
    answer = []
    h = []
    for s in score:
        hq.heappush(h, s)
        if len(h) > k: hq.heappop(h)
        answer.append(h[0])
    return answer