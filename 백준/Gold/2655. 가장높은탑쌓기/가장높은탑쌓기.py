import sys
input = sys.stdin.readline

N = int(input())

bricks = {}
for i in range(1, N+1):
    bricks[i] = list(map(int, input().split()))

sort_bricks = [(0,[10001,0,10001])] + sorted(bricks.items(), key = lambda item:item[1][0] ,reverse=True)

height = [0]*(N+1)
stack = [[]]*(N+1)

for i in range(1, N+1):
    max_height = 0
    idx = 0
    for j in range(i):
        if sort_bricks[i][1][2] < sort_bricks[j][1][2]:
            if max_height < height[j] + sort_bricks[i][1][1]:
                max_height = height[j] + sort_bricks[i][1][1]
                idx = j
    height[i] = max_height
    stack[i] = stack[idx].copy()
    stack[i].append(sort_bricks[i][0])
        
ans = stack[height.index(max(height))]
print(len(ans))
for i in range(1, len(ans)+1):
    print(ans[-i])