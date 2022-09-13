import sys
input = sys.stdin.readline

N = int(input())
soldier = [10000001] + list(map(int, input().split()))

dp = [0]*(N+1)

for i in range(1,N+1):
    max_cnt = 0
    for j in range(i):
        if soldier[i] < soldier[j]:
            max_cnt = max(max_cnt, dp[j]+1)
    dp[i] = max_cnt

print(N-max(dp))