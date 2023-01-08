import sys
input = sys.stdin.readline

INF = int(1e9)

# n: 도시의 개수
n = int(input())

# m: 버스의 개수
m = int(input())

# 버스의 정보 입력
bus = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    st, ed, cost = map(int, input().split())
    if bus[st][ed] == INF:
        bus[st][ed] = cost
    else:
        bus[st][ed] = min(bus[st][ed], cost)
        
for i in range(n+1):
    bus[i][i] = 0
    
# 플로이드-워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if bus[i][j] == INF:
            print(0, end = ' ')
        else:
            print(bus[i][j], end = ' ')
    print()