def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, ans):
        nonlocal answer
        if idx == n:
            if ans == target:
                answer += 1
            return
        
        dfs(idx + 1, ans + numbers[idx])
        dfs(idx + 1, ans - numbers[idx])
        
    dfs(0, 0)
    return answer