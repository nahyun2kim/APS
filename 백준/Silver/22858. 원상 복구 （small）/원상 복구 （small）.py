#구현 #시뮬레이션

import sys
input = sys.stdin.readline

# n: 카드의 개수, k: 카드를 섞은 횟수
n, k = map(int, input().split())

# 현재 카드 배치
now_cards = list(map(int, input().split()))

# 카드를 바꾸는 순서
d = list(map(int, input().split()))

for _ in range(k):
    cards = [0 for _ in range(n)]
    for i in range(n):
        cards[d[i]-1] = now_cards[i]
    now_cards = cards[:]

print(*now_cards)