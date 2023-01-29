import sys
input = sys.stdin.readline

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    x = find_parent(a)
    y = find_parent(b)
    if x != y:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

# 행성의 개수
n = int(input())

# 행성의 정보
x = []
y = []
z = []

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

# 인접 간선을 구하기 위한 정렬 작업
x.sort()
y.sort()
z.sort()

# 부모 정보 저장할 배열
parent = [i for i in range(n)]

# 연결할 수 있는 모든 경우의 수를 저장
edges = []
for i in range(1, n):
        edges.append((x[i][0] - x[i-1][0], x[i-1][1], x[i][1]))
        edges.append((y[i][0] - y[i-1][0], y[i-1][1], y[i][1]))
        edges.append((z[i][0] - z[i-1][0], z[i-1][1], z[i][1]))

# 비용 순으로 정렬 ( 오름차순 )
edges.sort()

# 최소 비용 구하기
ans = 0
for c, a, b in edges:
    x = find_parent(a)
    y = find_parent(b)
    if x != y:
        union(a, b)
        ans += c

print(ans)