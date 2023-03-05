# boj 13398 G5 연속합
# DP

import sys
input = sys.stdin.readline

n = int(input())

seq = list(map(int, input().split()))
dp = [x for x in seq]
sub_dp = [x for x in seq]

for i in range(1, n):
    dp[i] = max(dp[i-1]+seq[i], dp[i])

    # 현재 원소를 제거하거나, 이미 제거한 원소에 더하거나
    sub_dp[i] = max(dp[i-1], sub_dp[i-1]+seq[i])

print(max(max(dp), max(sub_dp)))