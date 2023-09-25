def solution(board, moves):
    answer = 0
    cols = [[] for _ in range(len(board))]
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board)):
            if board[i][j]:
                cols[j].append(board[i][j])
    basket = []
    for m in moves:
        if not cols[m-1]: continue
        if basket and basket[-1] == cols[m-1][-1]:
            basket.pop()
            answer += 2
        else:
            basket.append(cols[m-1][-1])
        cols[m-1].pop()
    return answer