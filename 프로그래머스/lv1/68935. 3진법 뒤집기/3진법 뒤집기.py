def solution(n):
    third = ''
    while n > 0:
        div, mod = divmod(n, 3)
        n = div
        third += str(mod)
    return int(third, 3)