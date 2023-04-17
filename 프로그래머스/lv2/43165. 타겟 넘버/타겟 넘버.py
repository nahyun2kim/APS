def solution(numbers, target):
    n = len(numbers)
    # 누적합
    cul_sum = [0]
    for num in numbers:
        cul_sum.append(cul_sum[-1] + num)
    answer = 0
    def dfs(idx, ans):
        nonlocal answer
        if idx == n:
            if ans == target:
                answer += 1
            return
        if ans < target and ans + cul_sum[-1] - cul_sum[idx] < target:
            return
        if ans > target and ans - cul_sum[-1] + cul_sum[idx] > target:
            return
        
        dfs(idx + 1, ans + numbers[idx])
        dfs(idx + 1, ans - numbers[idx])
        
    dfs(0, 0)
    return answer