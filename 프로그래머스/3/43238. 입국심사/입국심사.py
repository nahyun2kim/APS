def solution(n, times):
    answer = 987654321987654321
    st, ed = 1, n * max(times)
    while st <= ed:
        mid = (st + ed) // 2
        done = 0
        done = sum(mid // time for time in times)
        if done >= n:
            answer = min(answer, mid)
            ed = mid - 1
        elif done < n:
            st = mid + 1
    return answer