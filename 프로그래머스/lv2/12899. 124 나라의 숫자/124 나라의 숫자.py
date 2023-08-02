def solution(n):
    num = {0: "1", 1: "2", 2: "4"}
    answer = ''
    while n > 0:
        n -= 1
        n, mod = divmod(n, 3)
        answer += num[mod]
    return "".join(list(reversed(answer)))