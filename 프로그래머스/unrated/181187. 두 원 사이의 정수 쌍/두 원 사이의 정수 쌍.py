def solution(r1, r2):
    tmp1 = 0
    y = r1
    for i in range(1, r1):
        while (i*i + y*y) >= r1*r1:
            y -= 1
        tmp1 += y
    tmp1 = tmp1*4 + (r1-1)*4 + 1
    
    tmp2 = 0
    y = r2
    for i in range(1, r2):
        while (i*i + y*y) > r2*r2:
            y -=1
        tmp2 += y
    tmp2 = tmp2*4 + r2*4 + 1
    return tmp2 - tmp1