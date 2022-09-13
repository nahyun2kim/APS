N = int(input())
total = 0
houses = []

for _ in range(N):
    x, a = map(int, input().split())
    total += a
    houses.append((x, a))

cnt = 0
for pos, peo in sorted(houses, key = lambda x: x[0]):
    cnt += peo
    if cnt > total//2:
        print(pos)
        break