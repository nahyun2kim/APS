import heapq

# n: 카드 묶음의 수
n = int(input())

# 카드들
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

# 최소 비교 횟수
answer = 0

# cards의 길이가 2개 남을 때까지 진행,,,
while len(cards) > 2:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    
    plus = first + second
    heapq.heappush(cards, plus)
    
    answer += plus

# 처음부터 cards의 길이가 1개였다면, 비교횟수는 0
if len(cards) == 1:
    answer = 0
    
# 남은 두 개를 더해서 완성
else:
    answer += sum(cards)

# 출력
print(answer)