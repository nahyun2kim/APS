def solution(brown, yellow):
    rc = (brown + 4) // 2
    for i in range(3, rc-2):
        r = rc - i
        c = i
        if r*c - brown == yellow:
            return [r, c]
    return []