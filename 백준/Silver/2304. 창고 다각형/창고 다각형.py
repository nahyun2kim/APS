# boj 2304 S2 창고 다각형
# 자료 구조 # 브루트포스 # 스택

import sys
input = sys.stdin.readline

# 기둥의 개수
n = int(input())
cols = []
for _ in range(n):
    x, y = map(int, input().split())
    cols.append((x, y))

# x좌표로 정렬
cols_x = sorted(cols)
# 높이로 내림차순
cols_y = sorted(cols, key = lambda x:-x[1])

# 가장 높은 기둥
hx, hy = cols_y[0]
idx = cols_x.index((hx, hy))

area = hy

# 가장 높은 기둥 왼편
left_x, left_y = cols_x[0]
for i in range(1, idx+1):
    if cols_x[i][1] >= left_y:
        area += (cols_x[i][0] - left_x) * left_y
        left_x, left_y = cols_x[i]

# 가장 높은 기둥 오른편
right_x, right_y = cols_x[-1]
for i in range(len(cols)-1, idx-1, -1):
    if cols_x[i][1] >= right_y:
        area += (right_x - cols_x[i][0]) * right_y
        right_x, right_y = cols_x[i]

print(area)