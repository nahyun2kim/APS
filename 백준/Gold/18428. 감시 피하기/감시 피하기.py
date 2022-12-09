from itertools import combinations
import sys
input = sys.stdin.readline

# n: 복도의 길이
n = int(input())

# 복도의 정보
map_info = []
for _ in range(n):
    map_info.append(list(input().split()))

# 복도를 돌면서 선생님의 좌표와 빈칸의 좌표 저장
blanks = []
teachers = []
for i in range(n):
    for j in range(n):
        if map_info[i][j] == 'T':
            teachers.append((i, j))
        elif map_info[i][j] == 'X':
            blanks.append((i, j))

def check():
    for i,j in teachers:
        # 위쪽 검사
        up = i-1
        while up >= 0:
            if map_info[up][j] == 'S':
                return False
            elif map_info[up][j] == 'O':
                break
            up -= 1
            
        # 아래쪽 검사
        down = i+1
        while down < n:
            if map_info[down][j] == 'S':
                return False
            elif map_info[down][j] == 'O':
                break
            down += 1
            
        # 왼쪽 검사
        left = j-1
        while left >= 0:
            if map_info[i][left] == 'S':
                return False
            elif map_info[i][left] == 'O':
                break
            left -= 1
        
        # 오른쪽 검사
        right = j+1
        while right < n:
            if map_info[i][right] == 'S':
                return False
            elif map_info[i][right] == 'O':
                break
            right += 1
            
    return True


ans = "NO"
combi = combinations(blanks, 3)
for sel in combi:
    for i,j in sel:
        map_info[i][j] = 'O'
    if check():
        ans = "YES"
        break
    for i,j in sel:
        map_info[i][j] = 'X'
        
print(ans)