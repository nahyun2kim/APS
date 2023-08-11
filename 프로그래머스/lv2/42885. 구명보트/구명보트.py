import heapq

def solution(people, limit):
    people.sort(key = lambda x : -x)
    boat = []
    cnt = 0
    for i in people:
        if boat:
            last = heapq.heappop(boat)
            if last + i <= limit:
                cnt += 1
            else:
                heapq.heappush(boat, last)
                heapq.heappush(boat, i)
        else:
            boat.append(i)
    return cnt + len(boat)