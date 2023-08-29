def solution(n):
    return int("".join(map(str, sorted(str(n), reverse=True))))
