def solution(n):
    answer = 0
    third = ''
    while n > 0:
        div, mod = divmod(n, 3)
        n = div
        third = str(mod) + third
    for i in range(len(third)):
        answer += (3**i)*int(third[i])
    return answer