def solution(park, routes):
    delta = {'E':(0, 1), 'W':(0, -1), 'S':(1, 0), 'N':(-1, 0)}
    # 출발지 설정
    x = y = 0
    for i in range(len(park)):
        if 'S' in park[i]:
            x = i
            y = park[i].index('S')
    for r in routes:
        d, cnt = r.split()
        nx = x + delta[d][0] * int(cnt)
        ny = y + delta[d][1] * int(cnt)
        if 0 <= nx < len(park) and 0 <= ny < len(park[0]): # 구역을 안벗어난다면,,
            tx = x
            ty = y
            c = int(cnt)
            flag = True
            while c > 0:
                cx = tx + delta[d][0]
                cy = ty + delta[d][1]
                if park[cx][cy] == 'X':
                    flag = False
                    break
                tx = cx
                ty = cy
                c -= 1
            if flag:
                x = nx
                y = ny
    return [x, y]