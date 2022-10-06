import sys
input = sys.stdin.readline

# N: 우주신의 수, M: 이미 연결된 통로의 수
N, M = map(int, input().split())

pos = []
for _ in range(N):
    pos.append(list(map(float, input().split())))

# 간선의 정보
edges = []
for i in range(N-1):
    for j in range(i+1, N):
        tmp = ((pos[i][0]-pos[j][0])**2 + (pos[i][1]-pos[j][1])**2)**0.5
        edges.append((i+1, j+1, tmp))

# 대표자 저장
p = [i for i in range(N+1)]

# 대표자 찾는 함수
def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(a, b):
    a = find_set(a)
    b = find_set(b)
    p[max(a,b)] = min(a,b)

# 이미 연결된 통로
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

# 간선들 정렬
edges.sort(key = lambda x:x[2])

ans = 0
for i in range(len(edges)):
    st = find_set(edges[i][0])
    ed = find_set(edges[i][1])
    if p[st] != p[ed]:
        union(st, ed)
        ans += edges[i][2]


print('%.2f' %(ans))