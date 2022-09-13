N = int(input())
sche = []
for _ in range(N):
    t_i, s_i = map(int, input().split())
    sche.append((t_i, s_i))
sche = sorted(sche, key = lambda x : -x[1])
time = sche[0][1]
for t_i, s_i in sche:
    if time > s_i:
        time = s_i
    time -= t_i

if time < 0:
    print(-1)
else:
    print(time)