def solution(progresses, speeds):
    days = []
    for i in range(len(speeds)):
        if (100-progresses[i]) % speeds[i] == 0:
            days.append((100-progresses[i]) // speeds[i])
        else:
            days.append((100-progresses[i]) // speeds[i] + 1)
    answer = [0]
    now = days[0]
    for day in days:
        if now < day:
            answer.append(1)
            now = day
        else:
            answer[-1] += 1
    return answer