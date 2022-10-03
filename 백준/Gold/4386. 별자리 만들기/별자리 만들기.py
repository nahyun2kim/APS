import sys
input = sys.stdin.readline

N = int(input())
stars = []
for _ in range(N):
    stars.append(list(map(float, input().split())))

edges = [[0]*3 for _ in range(N*(N-1)//2)]
idx = 0
for i in range(N):
    for j in range(i+1,N):
        edges[idx][0] = i
        edges[idx][1] = j
        edges[idx][2] = ((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)**0.5
        idx += 1

# 간선 정렬(거리로 오름차순)
edges.sort(key=lambda x:x[2])
        
# 대표자를 저장할 p리스트
p = [i for i in range(N)]

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

# 간선을 N-1개 만큼 뽑자
pick = 0
ans = 0
for i in range(N*(N-1)//2):
    st = find_set(edges[i][0])
    ed = find_set(edges[i][1])
    if p[st] != p[ed]:
        p[find_set(ed)] = find_set(st)
        ans += edges[i][2]
        pick += 1
            
    if pick == N-1:
        break

print(round(ans, 2))