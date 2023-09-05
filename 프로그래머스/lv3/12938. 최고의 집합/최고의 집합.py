def solution(n, s):
    div, mod = divmod(s, n)
    if not div: return [-1]
    answer = [div] * n
    for i in range(1, mod+1):
        answer[-i] += 1
    return answer