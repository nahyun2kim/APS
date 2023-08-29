def solution(n):
    return int("".join(map(str, sorted(map(int, str(n)), reverse=True))))
