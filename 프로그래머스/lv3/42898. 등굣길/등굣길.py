def solution(m, n, puddles):
    arr = [[0]*m for _ in range(n)]
    for px, py in puddles:
        arr[py-1][px-1] = -1
    for i in range(m):
        if arr[0][i] == -1:
            break
        arr[0][i] = 1
    for i in range(n):
        if arr[i][0] == -1:
            break
        arr[i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            if not arr[i][j] == -1:
                up = 0 if arr[i-1][j] == -1 else arr[i-1][j]
                left = 0 if arr[i][j-1] == -1 else arr[i][j-1]
                arr[i][j] = up + left
    return arr[-1][-1] % 1000000007