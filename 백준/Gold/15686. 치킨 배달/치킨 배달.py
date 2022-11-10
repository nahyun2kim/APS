from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))
    
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

min_dist = 100000000
combi = list(combinations(chicken, m))

for comb in combi:
    dist = 0
    for hx, hy in house:
        min_d = 10000000
        for x, y in comb:
            min_d = min(min_d, (abs(hx-x)+abs(hy-y)))
        dist += min_d
        if dist >= min_dist:
            break
    min_dist = min(min_dist, dist)

print(min_dist)