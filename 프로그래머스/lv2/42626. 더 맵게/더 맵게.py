import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
        
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if not scoville:
            answer = -1
            break
        second = heapq.heappop(scoville)
        answer += 1
        heapq.heappush(scoville, first + 2*second)
    return answer