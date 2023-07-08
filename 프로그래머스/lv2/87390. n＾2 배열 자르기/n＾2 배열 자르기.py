def solution(n, left, right):
    answer = []
    st = left // n + 1
    ed = right // n + 1
    for i in range(st, ed+1):
        answer += [i]*i + [j+1 for j in range(i, n)]
    return answer[left%n:(ed-st)*n+right%n+1]