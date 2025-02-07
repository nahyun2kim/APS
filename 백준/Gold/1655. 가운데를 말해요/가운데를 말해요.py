import heapq
import sys
input = sys.stdin.readline

# 외치는 수 n
n = int(input())

lq = [] # 최대힙
rq = [] # 최소힙
for i in range(n):
  num = int(input())
  if len(lq) == len(rq):
    heapq.heappush(lq, -num)
  else:
    heapq.heappush(rq, num)

  # 만약 lq의 최대값보다 rq의 최솟값이 더 작다면 위치 교체
  if rq and -lq[0] > rq[0]:
    lq_value = heapq.heappop(lq)
    rq_value = heapq.heappop(rq)
    heapq.heappush(lq, -rq_value)
    heapq.heappush(rq, -lq_value)

  print(-lq[0])