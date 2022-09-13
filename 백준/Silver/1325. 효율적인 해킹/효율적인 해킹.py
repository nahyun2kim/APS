from collections import deque

N, M = map(int,input().split()) # 컴퓨터의 개수와, 신뢰관계 개수
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    arr[b].append(a)    # 신뢰관계 저장
    
def bfs(start):
    cnt= 1
    check= [False]*(N+1)
    check[start] = True # 처음 방문 노드를 방문했다고 지정
    dq = deque() # dq를 deque에 start노드만을 저장하고 시작
    dq.append(start)
    while dq:   # dq가 비어있을 때까지 반복하라
        node = dq.popleft()  
        for next in arr[node]:        #신뢰관계를 보며 다음 볼 노드 선정
            if not check[next]:     # 아직 방문한 노드가 아니라면,
                dq.append(next)        # 다음에 돌아보기 위해 dq에 저장해두고
                check[next] = True   # 방문했다고 표시
                cnt += 1
    return cnt

ans = []
for i in range(1,N+1):
    cnt = bfs(i)                 # 해킹할 수 있는 컴퓨터 수
    ans.append(cnt)          # 튜플로 해킹 시작한 노드와 컴퓨터 수 저장

    
for i in range(len(ans)):
    if ans[i] == max(ans):         # 컴퓨터 수가 저장해둔 최댓값과 같다면 출력
        print(i+1, end=" ")