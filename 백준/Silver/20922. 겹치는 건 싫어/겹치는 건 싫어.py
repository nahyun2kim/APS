N, K = map(int, input().split())
arr = list(map(str, input().split()))

start, end = 0, 0
answer = 0
counter = {}

while end < N:
    end_cnt = counter.get(arr[end], 0)
    if end_cnt < K:
        end_cnt += 1
        counter[arr[end]] = end_cnt
        end += 1
    else:
        start_cnt = counter.get(arr[start], 0)
        start_cnt -= 1
        counter[arr[start]] = start_cnt
        start += 1
        
    answer = max(answer, end - start)
print(answer)