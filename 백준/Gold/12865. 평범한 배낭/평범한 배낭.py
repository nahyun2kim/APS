import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]

item = {0: 0}
for i in range(N):
    new_item = bags[i]
    item_list = item.copy()
    for j in item_list.keys():
        if j + new_item[0] <= K:
            if j + new_item[0] in item_list.keys() and item_list[j+new_item[0]] >= item_list[j] + new_item[1]:
                continue
            else:
                item[j+new_item[0]] = item_list[j] + new_item[1]

print(max(item.values()))