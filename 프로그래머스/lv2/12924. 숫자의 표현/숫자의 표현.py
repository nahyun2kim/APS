def solution(n):
    ans = 0
    acc = [0]
    for i in range(1, n+1):
        acc.append(acc[i-1]+i)
    for i in range(n, 0, -1):
        if acc[i] < n:
            break
        for j in range(i-1, -1, -1):
            if acc[i] - acc[j] > n:
                break
            if acc[i] - acc[j] == n:
                ans += 1
                break
    return ans