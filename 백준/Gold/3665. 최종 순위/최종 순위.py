from collections import deque

# 테스트 케이스 수
t = int(input())
for _ in range(t):

    # 팀의 수
    n = int(input())

    # 위상정렬을 위한 배열
    indegree = [0 for _ in range(n+1)]

    # 작년 순위로 간선 배열 만들기
    last = list(map(int, input().split()))
    edges = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            edges[last[i]][last[j]] = 1
            indegree[last[j]] += 1

    # 순위가 바뀌는 작업
    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        if not edges[a][b]:
            edges[a][b] = 1
            edges[b][a] = 0
            indegree[b] += 1
            indegree[a] -= 1
        else:
            edges[a][b] = 0
            edges[b][a] = 1
            indegree[b] -= 1
            indegree[a] += 1

    q = deque([])

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    answer = []
    ans = ''
    while q:
        if len(q) > 1:
            ans = '?'
            break
        now = q.popleft()
        answer.append(now)
        for i in range(1, n+1):
            if edges[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if not len(answer) == n:
        ans = 'IMPOSSIBLE'

    if not ans == '':
        print(ans)
    else:
        for a in answer:
            print(a, end=' ')
        print()