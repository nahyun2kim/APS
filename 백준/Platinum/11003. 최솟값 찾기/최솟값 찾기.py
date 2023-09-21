from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
nums = list(map(int, input().split()))
answer = []

dq = deque()
for i, num in enumerate(nums):
    while dq and nums[dq[-1]] >= num:
        dq.pop()
    dq.append(i)
    if i - dq[0] == l:
        dq.popleft()
    print(nums[dq[0]], end=' ')