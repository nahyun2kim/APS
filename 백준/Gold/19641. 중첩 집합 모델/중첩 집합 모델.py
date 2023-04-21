import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(idx):
    global cnt
    lr[idx][0] = cnt
    cnt += 1
    edge = sorted(edges[idx])
    for x in edge:
        if not visit[x]:
            visit[x] = True
            dfs(x)
    lr[idx][1] = cnt
    cnt += 1


n = int(input())

edges = [[] for _ in range(n+1)]
visit = [False] * (n+1)
lr = [[0, 0] for _ in range(n+1)]

for _ in range(n):
    tmp = list(map(int, input().split()))
    edges[tmp[0]] = tmp[1:-1]

root = int(input())
visit[root] = True
cnt = 1

dfs(root)
for i in range(1, n+1):
    print(i, end=' ')
    print(*lr[i])