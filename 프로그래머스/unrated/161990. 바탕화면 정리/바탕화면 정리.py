def solution(wallpaper):
    answer = [100, 100, -1, -1]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                answer[0] = min(answer[0], i)
                answer[1] = min(answer[1], j)
                answer[2] = max(answer[2], i+1)
                answer[3] = max(answer[3], j+1)
    return answer