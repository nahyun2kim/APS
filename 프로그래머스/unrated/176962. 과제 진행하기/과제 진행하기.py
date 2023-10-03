def t2s(time):
    h, s = map(int, time.split(':'))
    return h*60 + s

def solution(plans):
    plans.sort(key = lambda x : x[1])
    complete = []
    pause = []
    for i in range(len(plans)):
        name, start, time = plans[i]
        if i < len(plans) - 1: # 제일 마지막 과제가 아니라면
            if t2s(start) + int(time) <= t2s(plans[i+1][1]):
                complete.append(name)
                remain = t2s(plans[i+1][1]) - t2s(start) - int(time)
                while pause and remain:
                    plan = pause.pop()
                    if plan[1] > remain:
                        pause.append((plan[0], plan[1] - remain))
                        remain = 0
                    else:
                        complete.append(plan[0])
                        remain -= plan[1]
            else:
                pause.append((name, int(time) - t2s(plans[i+1][1]) + t2s(start)))
        else:
            complete.append(name)
    while pause:
        plan = pause.pop()
        complete.append(plan[0])
    return complete