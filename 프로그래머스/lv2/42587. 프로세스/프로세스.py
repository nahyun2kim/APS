from collections import deque

def solution(priorities, location):
    first = max(priorities)
    cnt = 1
    q = deque([])
    for i in range(len(priorities)):
        if i == location:
            q.append((priorities[i], 1))
        else:
            q.append((priorities[i], 0))
    while q:
        now = q.popleft()
        if now[0] == first:
            if now[1]:
                break
            priorities.remove(first)
            first = max(priorities)
            cnt += 1
        else:
            q.append(now)
    return cnt