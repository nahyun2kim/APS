import queue
import sys
input = sys.stdin.readline

#1. 입력받기
N, M, V = map(int, input().split())
nodes = {}
    # 양방향으로 딕셔너리 배열로 넣어줌
for _ in range(M):
    n1, n2 = map(int, input().split())
    if n1 in nodes:
        nodes[n1].append(n2)
    else:
        nodes[n1] = [n2]
    if n2 in nodes:
        nodes[n2].append(n1)
    else:
        nodes[n2] = [n1]
    
def dfs(node):
    ans_dfs = []
    check_dfs = [0]*(N+1)
    stack = []
    stack.append(node)
    while stack:
        now = stack.pop()
        if check_dfs[now] != 1:
            ans_dfs.append(now)
            check_dfs[now] = 1
        if now in nodes:
            s_arr = sorted(nodes[now], reverse=True )
            for i in s_arr:
                if check_dfs[i] == 0:
                    stack.append(i)
    return list(map(str, ans_dfs))
                
def bfs(node):
    ans_bfs = []
    check_bfs = [0]*(N+1)
    q = queue.Queue()
    q.put(node)
    check_bfs[node] = 1
    while not q.empty():
        now = q.get()
        ans_bfs.append(now)
        if now in nodes:
            s_arr = sorted(nodes[now])
            for i in s_arr:
                if check_bfs[i] == 0:
                    check_bfs[i] = 1
                    q.put(i)
    return list(map(str, ans_bfs))
                
            
dfs(V)
bfs(V)

print(" ".join(dfs(V)))
print(" ".join(bfs(V)))