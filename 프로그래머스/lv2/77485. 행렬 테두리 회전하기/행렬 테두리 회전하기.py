def solution(rows, columns, queries):
    answer = []
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    arr = [[i+1 for i in range(columns*j, columns*(j+1))] for j in range(rows)]
    if len(queries) == 1:
        return [arr[queries[0][0]-1][queries[0][1]-1]]
    for x1, y1, x2, y2 in queries:
        temp = [arr[:] for arr in arr]
        d = 0
        x = x1 - 1
        y = y1 - 1
        min_val = 1000000
        while d < 4:
            nx = x + delta[d][0]
            ny = y + delta[d][1]
            if x1 - 1 <= nx < x2 and y1 - 1 <= ny < y2:
                temp[nx][ny] = arr[x][y]
                min_val = min(min_val, arr[x][y])
                x = nx
                y = ny
            else:
                d += 1
        answer.append(min_val)
        arr = temp
    return answer