def solution(triangle):
    n = len(triangle)
    dp = [[triangle[0][0]]] + [[0]*i for i in range(2, n+1)]
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == i:
                dp[i][j] = triangle[i][j] + dp[i-1][-1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])  
    return max(dp[-1])