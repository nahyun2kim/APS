import sys
input = sys.stdin.readline

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    x = find_parent(a)
    y = find_parent(b)
    if not x == y:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

# n: 집의 개수, m: 길의 개수
n, m = map(int, input().split())

# 부모 저장할 배열
parent = [i for i in range(n+1)]

# 길의 정보
road = []
for _ in range(m):
    a, b, c = map(int ,input().split())
    road.append((c, a, b))

# 유지비 정렬 ( 오름차순 )
road.sort()

# ans: 유지비 합, last: 그 중 가장 큰 간선
ans = 0
max_road = 0
for c, a, b in road:
    x = find_parent(a)
    y = find_parent(b)
    if x == y:
        continue
    else:
        union(a, b)
        ans += c
        max_road = c

print(ans - max_road)