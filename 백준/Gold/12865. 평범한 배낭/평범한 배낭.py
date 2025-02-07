import sys
input = sys.stdin.readline

# 물품의 수 n, 버틸수 있는 무게 k
n, k = map(int, input().split(' '))

items = []
for _ in range(n):

  # 각 물건의 무게 w, 가치 v
  w, v = map(int, input().split(' '))
  items.append((w, v))

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
  weight, value = items[i-1]
  for j in range(1, k + 1):

    # 가방에 넣을 수 없다면
    if weight > j:
      dp[i][j] = dp[i-1][j]

    else:
      dp[i][j] = max(dp[i-1][j - weight] + value, dp[i-1][j])

print(dp[n][k])