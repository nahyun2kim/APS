def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    for a in A:
        if a < B[0]:
            B.pop(0)
            answer += 1
    return answer