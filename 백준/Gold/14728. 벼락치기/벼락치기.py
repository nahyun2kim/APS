# boj 14728 G5 벼락치기
# DP # 배낭

import sys
input = sys.stdin.readline

# n: 단원 개수, t: 공부할 수 있는 총 시간
n, t = map(int, input().split())

dp = [[0]*(t+1) for _ in range(n+1)]

for i in range(1, n+1):
    # k: 단원 별 공부 시간, s: 배점
    k, s = map(int, input().split())

    for j in range(1, t+1):
        if j < k:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k] + s)

print(dp[n][t])
