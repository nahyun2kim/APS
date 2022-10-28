def solution(n, build_frame):
    cols = [[0]*(n+1) for _ in range(n+1)]
    rows = [[0]*(n+1) for _ in range(n+1)]
    
    def make(x,y,a):
        nonlocal cols, rows
        # 기둥 설치
        if a == 0:
            if y == 0 or rows[x][y] or cols[x][y-1] or (x>0 and rows[x-1][y]):
                return True
        # 보 설치
        elif a == 1:
            if y != 0 and cols[x][y-1] or (x < n and cols[x+1][y-1]) or (0<x<n and rows[x-1][y] and rows[x+1][y]):
                return True
            
        return False
    
    # 전수 조사
    def delete():
        nonlocal cols, rows
        for i in range(n+1):
            for j in range(n+1):
                if cols[i][j] and not make(i,j,0):
                    return False
                if rows[i][j] and not make(i,j,1):
                    return False
                
        return True
    
    for x,y,a,b in build_frame:
        if b == 1:
            if a == 0 and make(x,y,a):
                cols[x][y] = 1
            elif a == 1 and make(x,y,a):
                rows[x][y] = 1
        
        elif b == 0:
            if a == 0:
                cols[x][y] = 0
                if not delete():
                    cols[x][y] = 1
            elif a == 1:
                rows[x][y] = 0
                if not delete():
                    rows[x][y] = 1
                    
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if cols[i][j]:
                answer.append([i,j,0])
            if rows[i][j]:
                answer.append([i,j,1])
    
    return answer