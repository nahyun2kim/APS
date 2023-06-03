import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
edges = [[0, 0] for _ in range(n+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    if not b == -1:
        edges[a][0] = b
    if not c == -1:
        edges[a][1] = c

visit = [True] + [False]*n
answer = []
in_order = []
def move(node):
    global answer
    answer.append(node)
    if not edges[node][0] == 0:
        move(edges[node][0])
        answer.append(node)
    in_order.append(node)
    if not edges[node][1] == 0:
        move(edges[node][1])
        if False in visit:
            answer.append(node)
    visit[node] = True

move(1)
while answer[-1] != in_order[-1]:
    answer.pop()


print(len(answer) - 1)