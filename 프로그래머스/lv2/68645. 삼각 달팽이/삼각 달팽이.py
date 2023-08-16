def solution(n):
    num = n * (n + 1) // 2
    t = [[0]*i for i in range(1, n+1)]
    delta = [[1, 0], [0, 1], [-1, -1]]
    idx = 1
    x = y = d = 0
    while idx <= num:
        t[x][y] = idx
        nx = x + delta[d][0]
        ny = y + delta[d][1]
        if 0 <= nx < n and 0 <= ny <= nx and not t[nx][ny]:
            x = nx
            y = ny
        else:
            d = d + 1 if d < 2 else 0
            x = x + delta[d][0]
            y = y + delta[d][1]
        idx += 1
    return sum(t, [])