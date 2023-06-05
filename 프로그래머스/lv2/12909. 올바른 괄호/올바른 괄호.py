from collections import deque
def solution(s):
    s = deque(list(s))
    if len(s) % 2 != 0:
        return False
    left = []
    while s:
        if s.popleft() == '(':
            left.append('(')
        else:
            if not left:
                return False
            left.pop()
    if left:
        return False
    return True