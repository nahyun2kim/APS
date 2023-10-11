def t2m(time):
    h, m = map(int, time.split(':'))
    return h*60 + m

def m2t(minute):
    h, m = map(str, (divmod(minute, 60)))
    return h.zfill(2) + ':' + m.zfill(2)

def solution(n, t, m, timetable):
    table = [t2m(time) for time in sorted(timetable)]
    time = 540 # 09:00
    for i in range(time, time+t*(n-1), t):
        cnt = 1
        while table and cnt <= m:
            if table[0] > i:
                break
            table.pop(0)
            cnt += 1
    if not table or table[0] > time+t*(n-1):
        return m2t(time + t*(n-1))
    cnt = 0
    while table and cnt < m:
        tmp = table.count(table[0])
        if cnt + tmp >= m:
            return m2t(table[0] - 1)
        cnt += tmp
        for _ in range(tmp):
            table.pop(0)   
    return m2t(time + t*(n-1))