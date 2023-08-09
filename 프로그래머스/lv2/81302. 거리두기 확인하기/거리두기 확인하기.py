def solution(places):
    answer = []
    def check(i, j, place, visit):
        delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and not visit[ni][nj]:
                visit[ni][nj] = 1
                if place[ni][nj] == 'P':
                    return False
                elif place[ni][nj] == 'O':
                    for dx, dy in delta:
                        x = ni + dx
                        y = nj + dy
                        if 0 <= x < 5 and 0 <= y < 5 and not visit[x][y]:
                            visit[x][y] = 1
                            if place[x][y] == 'P':
                                return False
        return visit
        
    for place in places:
        visit = [[0]*5 for _ in range(5)]
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    visit[i][j] = 1
                    if check(i, j, place, visit) == False:
                        flag = False
                        break
            if not flag: break
        answer.append(1 if flag else 0)
    return answer