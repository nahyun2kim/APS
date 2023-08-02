from collections import deque

def solution(maps):
    maps = [list(arr) for arr in maps]
    answer = []
    n = len(maps)
    m = len(maps[0])
    def island(i, j):
        delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        day = int(maps[i][j])
        maps[i][j] = 'X'
        q = deque([(i, j)])
        while q:
            i, j = q.popleft()
            for di, dj in delta:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m and not maps[ni][nj] == 'X':
                    day += int(maps[ni][nj])
                    maps[ni][nj] = 'X'
                    q.append((ni, nj))
        return day
    for i in range(n):
        for j in range(m):
            if not maps[i][j] == 'X':
                day = island(i, j)
                answer.append(day)
    return sorted(answer) if answer else [-1]