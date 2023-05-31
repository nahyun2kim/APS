def solution(storey):
    storey = str(storey)
    answer = 123456789
    
    def solve(idx, up, cnt):
        nonlocal answer
        if idx == -1:
            answer = min(answer, cnt + up)
            return
        num = int(storey[idx]) + up
        if num > 5:
            solve(idx - 1, 1, cnt + (10 - num))
        elif num < 5:
            solve(idx - 1, 0, cnt + num)
        else:
            solve(idx - 1, 0, cnt + 5)
            solve(idx - 1, 1, cnt + 5)
    
    solve(len(storey)-1, 0, 0)
    return answer