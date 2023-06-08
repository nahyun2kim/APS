def solution(arr1, arr2):
    n = len(arr1)
    x = len(arr1[0])
    m = len(arr2[0])
    answer = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            value = 0 
            for k in range(x):
                value += arr1[i][k] * arr2[k][j]
            answer[i][j] = value
    return answer