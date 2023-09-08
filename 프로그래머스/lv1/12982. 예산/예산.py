def solution(d, budget):
    d.sort()
    total = 0
    for i in range(len(d)):
        if total + d[i] > budget:
            return i
        total += d[i]
    return len(d)