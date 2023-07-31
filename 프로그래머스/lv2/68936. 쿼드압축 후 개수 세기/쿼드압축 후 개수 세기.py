from collections import Counter as cnt

def solution(arr):
    answer = []
    def divide(arr):
        nonlocal answer
        n = len(arr)
        new = [[], [], [], []]
        for i in range(n):
            if i < n // 2:
                new[0].append(arr[i][:n//2])
                new[1].append(arr[i][n//2:])
            else:
                new[2].append(arr[i][:n//2])
                new[3].append(arr[i][n//2:])
        for row in new:
            check = []
            for r in row:
                check += r
                check = list(set(check))
            if not len(check) == 1:
                divide(row)
            else:
                answer.append(check[0])
    
    first = []
    for a in arr:
        first += a
        first = list(set(first))
    if len(first) == 1:
        return [1 if first[0] == 0 else 0, 1 if first[0] == 1 else 0]
    
    divide(arr)
    return [cnt(answer)[0], cnt(answer)[1]]
