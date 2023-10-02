def find(i, rep):
    if not rep[i] == i:
        rep[i] = find(rep[i], rep)
    return rep[i]

def union(a, b, rep):
    a = find(a, rep)
    b = find(b, rep)
    if a < b:
        rep[b] = a
    else:
        rep[a] = b

def solution(n, wires):
    answer = 123456789
    area = []
    for w in range(len(wires)):
        root = {}
        wire = wires[:]
        wire.pop(w)
        rep = [i for i in range(n+1)]
        for a, b in wire:
            if find(a, rep) != find(b, rep):
                union(a, b, rep)
        for i in range(1, len(rep)):
            if find(rep[i], rep) in root:
                root[find(rep[i], rep)] += 1
            else:
                root[find(rep[i], rep)] = 1
        area = list(root.values())
        answer = min(answer, abs(area[0] - area[1]))
    return answer