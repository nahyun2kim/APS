N, K = map(int, input().split())
doll = list(map(int, input().split()))+[0]

start, end = 0, 0
cnt = 0
ans = 1000000

while start <= end and end <= N:
    if cnt < K:
        if doll[end] == 1:
            cnt += 1
        end += 1
    else:
        ans = min(ans, end-start)
        if doll[start] == 1:
            cnt -= 1
        start += 1

if ans == 1000000:
    print(-1)
else:
    print(ans)