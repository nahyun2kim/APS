def addTime(now, add):
    m, s = now[0], now[1]
    s += add
    if s >= 60:
        m += 1
        s -= 60
    elif s < 0 and m > 0:
        m -= 1
        s += 60
    elif s < 0 and m == 0:
        s = 0
    return [m, s]


def isOpening(st, ed, now):
    if st[0] == ed[0]:
        return True if st[0] == now[0] and st[1] <= now[1] <= ed[1] else False
    if st[0] == now[0] and st[1] <= now[1]: return True
    if st[0] < now[0] < ed[0]: return True
    if now[0] == ed[0] and now[1] <= ed[1]: return True
    return False
    

def isEnd(ed, now):
    if now[0] > ed[0] or (now[0] == ed[0] and now[1] > ed[1]):
        return True
    return False
    
    
def toString(time):
    m, s = time[0], time[1]
    m = str(m) if m >= 10 else '0' + str(m)
    s = str(s) if s >= 10 else '0' + str(s)
    return ':'.join([m, s])


def solution(video_len, pos, op_start, op_end, commands):
    video = list(map(int, video_len.split(':')))
    pos = list(map(int, pos.split(':')))
    ost = list(map(int, op_start.split(':')))
    oed = list(map(int, op_end.split(':')))
    if (isOpening(ost, oed, pos)):
        pos = oed
    for command in commands:
        pos = addTime(pos, 10 if command == 'next' else -10)
        if (isOpening(ost, oed, pos)):
            pos = oed
        if (isEnd(video, pos)):
            pos = video
    return toString(pos)