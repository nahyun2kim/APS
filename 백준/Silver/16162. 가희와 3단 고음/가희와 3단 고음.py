# boj 16162 S4 가희와 3단 고음
# 그리디

import sys
input = sys.stdin.readline

# n: 음의 개수, a: 첫항, d: 공차
n, a, d = map(int, input().split())

pitch = list(map(int, input().split()))

ans = 0
check = a
for p in pitch:
    if p == check:
        ans += 1
        check += d

print(ans)