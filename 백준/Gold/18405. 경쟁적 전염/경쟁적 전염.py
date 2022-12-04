import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
virus = []
for _ in range(n):
    virus.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

h = []
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for t in range(s):
    for i in range(n):
        for j in range(n):
            if virus[i][j] > 0:
                heapq.heappush(h, (virus[i][j], i, j))
                
    if len(h) == n*n:
        break
        
    while h:
        num, i, j = heapq.heappop(h)
        for d in range(4):
            di = i + delta[d][0]
            dj = j + delta[d][1]
            if 0<=di<n and 0<=dj<n and virus[di][dj] == 0:
                virus[di][dj] = num

print(virus[x-1][y-1])