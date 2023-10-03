def find(i, parent):
    if parent[i] != i:
        parent[i] = find(parent[i], parent)
    return parent[i]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b: parent[b] = a
    else: parent[a] = b
    
def solution(n, costs):
    costs.sort(key = lambda x : x[2])
    parent = [i for i in range(n)]
    answer = 0
    for a, b, cost in costs:
        if not find(a, parent) == find(b, parent):
            answer += cost
            union(a, b, parent)
            if parent.count(parent[0]) == n:
                break
    return answer