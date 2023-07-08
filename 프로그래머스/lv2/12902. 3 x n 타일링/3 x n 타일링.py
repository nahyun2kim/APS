def solution(n):
    d = [1, 3, 11] + [0]*(n//2 - 2)
    for i in range(3, n//2 + 1):
        d[i] = 3 * d[i-1] + 2 * sum(d[:i-1])
        d[i] %= 1000000007
    return d[n//2]