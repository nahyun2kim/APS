N, S, M = map(int, input().split())
vol_list = list(map(int, input().split()))

vol = [S]
for i in range(len(vol_list)):
    temp = []
    while vol:
        new = vol.pop()
        if new-vol_list[i] >= 0 and new-vol_list[i] not in temp:
            temp.append(new-vol_list[i])
        if new+vol_list[i] <= M and new+vol_list[i] not in temp:
            temp.append(new+vol_list[i])
    if not temp:
        break
    vol = temp

if not vol:
    print(-1)
else:
    print(max(vol))