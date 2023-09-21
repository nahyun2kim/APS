from collections import deque
def solution(stones, k):
    answer = 987654321
    dq = deque([])
    for i, s in enumerate(stones):
        while dq and stones[dq[-1]] <= s:
            dq.pop()
        dq.append(i)
        if i - dq[0] == k:
            dq.popleft()
        if i + 1 >= k:
            answer = min(answer, stones[dq[0]])
    return answer