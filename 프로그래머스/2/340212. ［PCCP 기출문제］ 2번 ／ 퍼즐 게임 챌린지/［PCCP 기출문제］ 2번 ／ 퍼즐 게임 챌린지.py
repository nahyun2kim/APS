def cal_time(diff, time_prev, time_cur, level):
    sub = diff - level if diff > level else 0
    return (time_cur + time_prev) * sub + time_cur

def solution(diffs, times, limit):
    times = [0] + times
    min_level, max_level = 1, max(diffs)
    
    while min_level < max_level:
        mid = (min_level + max_level) // 2
        time = 0
        for i in range(len(diffs)):
            time += cal_time(diffs[i], times[i], times[i+1], mid)
            
        if time <= limit:
            max_level = mid
        else:
            min_level = mid + 1
    return min_level