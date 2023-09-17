def solution(n, stations, w):
    answer = 0
    st = 1
    for s in stations:
        if s - w > st:
            div, mod = divmod((s - w - st), (2*w + 1))
            answer += div
            answer += 1 if mod else 0
        st = s + w + 1
    if stations[-1] + w < n:
        div, mod = divmod((n - stations[-1] - w), (2*w + 1))
        answer += div
        answer += 1 if mod else 0
    return answer