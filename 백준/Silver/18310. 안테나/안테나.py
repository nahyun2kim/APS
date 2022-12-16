import sys
input = sys.stdin.readline

# n: 집의 수
n = int(input())

# 안테나를 설치할 수 있는 위치 값
pos = list(map(int, input().split()))

# 초기 정렬 (위치를 기준으로 오름차순)
pos.sort()

# 맨 앞에 안테나를 설치했을 때 거리의 합
dist = sum(pos) - (pos[0] * n)
ans = dist
idx = 0

# 안테나의 위치를 옯기며 거리 비교
for i in range(1, n):
    dist += (pos[i] - pos[i-1])*(2*i - n)
    if ans > dist:
        ans = dist
        idx = i

print(pos[idx])