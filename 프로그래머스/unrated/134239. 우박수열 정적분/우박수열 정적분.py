def solution(k, ranges):
    graph = [k]
    area = []
    while k > 1:
        k = k // 2 if k % 2 == 0 else 3*k + 1
        area.append((graph[-1]+k)*0.5)
        graph.append(k)
    area_sum = [0]
    for a in area:
        area_sum.append(area_sum[-1]+a)
    answer = []
    for st, ed in ranges:
        ed += len(area)
        answer.append(-1 if ed < st else area_sum[ed] - area_sum[st])
    return answer