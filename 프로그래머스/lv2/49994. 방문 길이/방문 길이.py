def solution(dirs):
    visit = []
    move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    x = 5
    y = 5
    for d in dirs:
        nx = x + move[d][0]
        ny = y + move[d][1]
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            r1 = str(x) + str(nx) + '@' + str(y) + str(ny)
            r2 = str(nx) + str(x) + '@' + str(ny) + str(y)
            visit.append(r1)
            visit.append(r2)
            x = nx
            y = ny
    visit = set(visit)
    return len(visit) // 2