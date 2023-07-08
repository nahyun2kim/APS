def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    def erase(arr):
        tmp = [a[:] for a in arr]
        flag = False
        for i in range(m-1):
            for j in range(n-1):
                if arr[i][j] != '@' and arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1]:
                    flag = True
                    tmp[i][j] = tmp[i+1][j] = tmp[i][j+1] = tmp[i+1][j+1] = '@'
        if not flag:
            return False
        res = [['@' for _ in range(n)] for _ in range(m)]
        for j in range(n):
            idx = m-1
            for i in range(m-1, -1, -1):
                if not tmp[i][j] == '@':
                    res[idx][j] = tmp[i][j]
                    idx -= 1
        return res
    while True:
        new_board = erase(board)
        if not new_board:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == '@':
                        answer += 1
            break
        else:
            board = new_board
    
    return answer