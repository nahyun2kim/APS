import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int,input().split()))

dp = [0]*(N+1)
for i in range(N+1):
    maxcnt = 0
    for j in range(i):
        if arr[i] > arr[j]:
            maxcnt = max(maxcnt, dp[j]+1)
    dp[i] = maxcnt

print(max(dp))