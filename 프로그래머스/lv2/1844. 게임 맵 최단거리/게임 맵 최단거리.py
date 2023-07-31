from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visit = [[0]*m for _ in range(n)]
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    answer = -1
    q = deque([(0, 0, 1)])
    while q:
        x, y, cnt = q.popleft()
        if x == n-1 and y == m-1:
            answer = cnt
            break
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny, cnt + 1))
    return answer