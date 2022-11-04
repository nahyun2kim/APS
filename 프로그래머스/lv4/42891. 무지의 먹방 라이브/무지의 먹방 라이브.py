import heapq

def solution(food_times, k):
    n = len(food_times)  # 남은 음식의 수

    # 음식을 다 먹는 시간보다 k가 클 경우 -1 반환
    if sum(food_times) <= k:
        return -1

    # 우선순위 큐에 음식을 먹는시간과 인덱스를 넣어주자
    h = []
    for i in range(n):
        heapq.heappush(h, (food_times[i], i))

    # 지난 시간
    time = 0
    # 최소 시간
    min_sec = h[0][0]
    ans = 0
    while True:
        if (min_sec - time) * n > k:
            ans = k % n
            break
        k -= (min_sec - time) * n
        time = min_sec
        heapq.heappop(h)
        n -= 1

        min_sec = h[0][0]

    # 인덱스 번호로 정렬
    h.sort(key=lambda x: x[1])
    return h[ans][1] + 1