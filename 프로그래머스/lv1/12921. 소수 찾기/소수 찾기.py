def solution(n):
    answer = 0
    num = [0]*(n+1)
    for i in range(2, n+1):
        if num[i]: continue
        answer += 1
        for j in range(i, n+1, i):
            num[j] = 1
    return answer