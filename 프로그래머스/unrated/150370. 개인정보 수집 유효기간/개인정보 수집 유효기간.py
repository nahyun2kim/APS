def plus(day, term):
    y, m, d = map(int, day.split('.'))
    m += term
    while m > 12:
        y += 1
        m -= 12
    return y, m, d-1

def solution(today, terms, privacies):
    answer = []
    terms = {i[0]:int(i[2:]) for i in terms}
    ty, tm, td = map(int, today.split('.'))
    for i, p in enumerate(privacies):
        day, t = p.split()
        py, pm, pd = plus(day, terms[t])
        if ty > py or (ty == py and tm > pm) or (ty == py and tm == pm and td > pd):
            answer.append(i + 1)
    return answer