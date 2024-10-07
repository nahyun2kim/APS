def solution(board, h, w):
    answer = 0
    n = len(board)
    delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dx, dy in delta:
        if 0 <= h + dx < n and 0 <= w + dy < n and board[h+dx][w+dy] == board[h][w]:
            answer += 1
    return answer