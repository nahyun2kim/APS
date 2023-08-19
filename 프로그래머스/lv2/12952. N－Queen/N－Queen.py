def check(idx, queen):
    for i in range(idx):
        if queen[idx] == queen[i] or idx-i == abs(queen[idx] - queen[i]):
            return False
    return True

def solution(n):
    queen = [0] * n
    def dfs(idx):
        if idx == n:
            return 1
        cnt = 0
        for i in range(n):
            queen[idx] = i
            if check(idx, queen):
                cnt += dfs(idx + 1)
        return cnt
    return dfs(0)