def find_parents(sub, node):
    parents= []
    parents.append(node)
    while True:
        if sub[node] == 0:
            break
        node = sub[node]
        parents.append(node)    
    return parents

T = int(input()) # 테스트 케이스의 수
for _ in range(T):
    N = int(input()) # 노드의 개수 N
    sub = [0]*(N+1)
    for _ in range(N-1): # 간선의 개수는 N-1개 만큼 생성됨
        a, b = map(int, input().split()) # a가 b의 부모
        sub[b] = a   # 자식한테 부모정보 저장
    nodeA, nodeB = map(int, input().split())
    parentsA = find_parents(sub, nodeA)
    parentsB = find_parents(sub, nodeB)
    
    ans = 0
    for i in parentsA:
        for j in parentsB:
            if i == j:
                ans = i
                break
        if ans != 0:
            break
    print(ans)