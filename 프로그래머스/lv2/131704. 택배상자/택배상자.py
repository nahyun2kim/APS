def solution(order):
    idx = 1
    cnt = 0
    sub = []
    while cnt < len(order):
        if order[cnt] == idx:
            cnt += 1
            idx += 1
        elif order[cnt] > idx:
            sub.append(idx)
            idx += 1
        else:
            if sub[-1] == order[cnt]:
                sub.pop()
                cnt += 1
            else:
                break
    return cnt