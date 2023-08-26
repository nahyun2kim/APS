import heapq as hq

def solution(operations):
    maxi = []
    mini = []
    for o in operations:
        a, b = o.split()
        if a == 'I':
            hq.heappush(maxi, int(b)*-1)
            hq.heappush(mini, int(b))
        else:
            if not maxi:
                continue
            elif b == '1':
                hq.heappop(maxi)
                mini.pop()
            else:
                hq.heappop(mini)
                maxi.pop()
    if maxi:
        return [(-1)*maxi[0], mini[0]]
    else:
        return [0, 0]