def solution(n):
    idx = 0
    l = int(n)
    num = {0: "1", 1: "2", 2: "4"}
    answer = ''
    while l > 0:
        idx += 1
        l -= 3 ** idx
    n = l + 3 ** idx - 1
    while True:
        n, mod = divmod(n, 3)
        answer += num[mod]
        if len(answer) == idx:
            break
    return "".join(list(reversed(answer)))