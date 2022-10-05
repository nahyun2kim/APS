import sys
input = sys.stdin.readline

# N: 건물의 개수, M: 도로의 개수
N, M = map(int, input().split())

# 도로의 정보 입력
road = []
road_cost = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    road.append([a, b, c])
    road_cost += c

# 크루스칼
p = [i for i in range(N+1)]

# 가중치로 오름차순 정렬
road.sort(key=lambda x:x[2])

def find_set(x):
    if not p[x] == x:
        p[x] = find_set(p[x])
    return p[x]

#간선을 N-1개만큼 뽑자
pick = 0
ans = 0

for i in range(M):
    st = find_set(road[i][0])
    ed = find_set(road[i][1])
    
    if p[st] != p[ed]:
        p[find_set(ed)] = find_set(st)
        ans += road[i][2]
        pick += 1
    
    if pick == N-1:
        break

if not pick == N-1:
    print(-1)
else:
    print(road_cost - ans)