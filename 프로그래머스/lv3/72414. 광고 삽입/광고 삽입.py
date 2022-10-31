def solution(play_time, adv_time, logs):
    n = switch_sec(play_time)
    time = [0]*(n+1)
    for log in logs:
        st, ed = log.split('-')
        time[switch_sec(st)] += 1
        time[switch_sec(ed)] -= 1
    for i in range(n):
        time[i+1] += time[i]
    for i in range(n):
        time[i+1] += time[i]
    
    init = switch_sec(adv_time)
    value = time[init-1]
    max_value = value
    adv_st = 0
    for i in range(len(time)-init):
        value = time[i+init] - time[i]
        if max_value < value:
            max_value = value
            adv_st = i+1
    
    return switch_time(adv_st)

def switch_sec(time):
    h,m,s = map(int, time.split(':'))
    return h*3600 + m*60 + s

def switch_time(sec):
    h = sec // 3600
    m = (sec%3600) // 60
    s = (sec%3600) % 60
    return str(h).zfill(2) +':'+ str(m).zfill(2) +':'+ str(s).zfill(2)
                