from collections import deque

def shortest_path(maps, sx, sy, target):
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    n, m = len(maps), len(maps[0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([(sx, sy, 0)])
    visit[sx][sy] = 1
    distance = -1
    
    while q:
        x, y, cnt = q.popleft()
        if maps[x][y] == target:
            distance = cnt
            break
        
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny, cnt + 1))
    
    return distance

def solution(maps):
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # 1. 행, 열의 길이 구하기
    n, m = len(maps), len(maps[0])
    
    # 2. 시작점, 레버 구하기
    sx, sy = 0, 0
    lx, ly = 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j
                
    # 3. 시작점에서 레버까지 최단 거리 구하기
    start_to_lever = shortest_path(maps, sx, sy, 'L')
    
    # 3-1. 레버까지 도달할 수 없다면 -1 return
    if start_to_lever == -1:
        return -1

    # 4. 레버에서 출구까지 최단 거리 구하기
    lever_to_exit = shortest_path(maps, lx, ly, 'E')
    
    # 4-1. 출구까지 도달할 수 없다면 -1 return
    if lever_to_exit == -1:
        return -1
    
    return start_to_lever + lever_to_exit