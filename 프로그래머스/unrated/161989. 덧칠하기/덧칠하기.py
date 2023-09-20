def solution(n, m, section):
    paint = []
    for s in section:
        if paint and s < paint[-1] + m:
            continue
        paint.append(s)
    return len(paint)