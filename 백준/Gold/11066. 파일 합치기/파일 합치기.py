import sys
input = sys.stdin.readline
INF = int(1e9)

T = int(input())

for _ in range(T):
  K = int(input())
  files = [0] + list(map(int, input().split(' ')))
  subs = [0 for _ in range(K + 1)]
  for i in range(1, K + 1):
    subs[i] = subs[i - 1] + files[i]

  dp = [[0] * (K + 1) for _ in range(K + 1)]
  for cnt in range(1, K):
    for st in range(1, K - cnt + 1):
      ed = st + cnt
      tmp = INF
      for mid in range(st, ed):
        tmp = min(tmp, dp[st][mid] + dp[mid + 1][ed])
      dp[st][ed] = tmp + subs[ed] - subs[st - 1]

  print(dp[1][K])