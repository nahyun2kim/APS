import queue
import sys
input = sys.stdin.readline

#1. 입력 
N, M = map(int, input().split()) # NxM 의 미로
maze = [[] for _ in range(N)]
for i in range(N):
    temp = input()
    for j in range(M):
        maze[i].append(int(temp[j]))


#2. 방문할때 카운트를 기록할 리스트
check = [[0]*M for _ in range(N)]


#3. 도착위치까지 탐색 
def find_end(i, j): 
    q = queue.Queue()
    q.put([i,j])
    check[i][j] = 1

    # 차례차례 큐에 넣어놓고 큐가 빌때까지 진행
    while not q.empty():
        
        now = q.get()
        x = now[0]
        y = now[1]

        #상하좌우 탐색 (미로를 벗어나지 않고, 방문했지않고, 길이 있는경우)
        if x-1 >=0 and check[x-1][y] == 0 and maze[x-1][y] == 1:
            check[x-1][y] = check[x][y]+1
            q.put([x-1,y])

        if x+1 < N and check[x+1][y] == 0 and maze[x+1][y] == 1:
            check[x+1][y] = check[x][y]+1
            q.put([x+1,y])

        if y-1 >=0 and check[x][y-1] == 0 and maze[x][y-1] == 1:
            check[x][y-1] = check[x][y]+1
            q.put([x,y-1])

        if y+1 < M and check[x][y+1] == 0 and maze[x][y+1] == 1:
            check[x][y+1] = check[x][y]+1
            q.put([x,y+1])

#4. 함수실행 후 출력
find_end(0,0)
print(check[N-1][M-1])