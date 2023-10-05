def solution(jobs):
    l = len(jobs)
    t = 0
    task = 0
    jobs.sort(key = lambda x : x[1])
    while jobs:
        for i in jobs:
            if i[0] <= t:
                jobs.remove(i)
                t += i[1] - 1
                task += t - i[0] +1
                break
        t += 1
    return task // l