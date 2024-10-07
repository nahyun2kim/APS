def solution(n, roads, sources, destination):
    # min_road: 최단거리 visit: 방문 여부
    min_road = [-1 if i!=destination else 0 for i in range(n + 1)]
    visit = [0 if i!=destination else 1 for i in range(n+1)]
    
    # 도로 정보 dict
    road = {}
    for a, b in roads:
        if a not in road:
            road[a] = []
        if b not in road:
            road[b] = []
        road[a].append(b)
        road[b].append(a)
        
    # destination에서 거꾸로 출발
    q = [(destination, 0)]
    while q:
        st, now = q.pop(0)
        
        if not st in road:
            continue
            
        for nxt in road[st]:
            if not visit[nxt]:
                min_road[nxt] = now + 1
                visit[nxt] = 1
                q.append((nxt, now + 1))
            
    # sources에 맞게 answer 입력
    answer = []
    for source in sources:
        answer.append(min_road[source])

    return answer