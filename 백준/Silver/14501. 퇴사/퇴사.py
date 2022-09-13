import sys
input = sys.stdin.readline

N = int(input())
task = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]

profit = [0]*(N+1)
for i in range(1, N+1):
    max_profit = 0
    for j in range(i):
        if j + task[j][0] <= i and i + task[i][0] <= N+1:
            max_profit = max(max_profit, profit[j]+task[i][1])
    profit[i] = max_profit

print(max(profit))