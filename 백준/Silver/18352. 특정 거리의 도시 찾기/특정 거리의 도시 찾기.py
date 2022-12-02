from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
edge = {}
for _ in range(m):
    a, b = map(int, input().split())
    if a in edge.keys():
        edge[a].append(b)
    else:
        edge[a] = [b]
visit = [False]*(n+1)
dq = deque([(x,0)])
visit[x] = True
ans = []
while dq:
    now, cnt = dq.popleft()
    if cnt == k:
        ans.append(now)
    if now in edge.keys():
        for i in edge[now]:
            if not visit[i]:
                visit[i] = True
                dq.append((i,cnt+1))

if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)