def solution(n, arr1, arr2):
    arr1 = ['0'*(n - len(bin(a)[2:])) + bin(a)[2:] for a in arr1]
    arr2 = ['0'*(n - len(bin(a)[2:])) + bin(a)[2:] for a in arr2]
    answer = []
    for a, b in zip(arr1, arr2):
        s = ''
        for i in range(n):
            s += '#' if a[i] == '1' or b[i] == '1' else ' '
        answer.append(s)
    return answer