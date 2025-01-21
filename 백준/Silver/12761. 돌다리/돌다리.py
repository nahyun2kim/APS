from collections import deque

# a, b: 콩콩이의 힘, m: 동규위치, n: 주미위치
a, b, m, n = map(int, input().split(' '))

dy = [1, -1, a, -a, b, -b, a, b]
cnt = [0 for _ in range(100001)]
visit = [0 for _ in range(100001)]

q = deque([m])
visit[m] = 1

while q:
  now = q.popleft()
  for i in range(8):
    if i < 6:
      next = now + dy[i]
    else:
      next = now * dy[i]

    if 0 <= next <= 100000 and not visit[next]:
      q.append(next)
      visit[next] = 1
      cnt[next] = cnt[now] + 1

print(cnt[n])