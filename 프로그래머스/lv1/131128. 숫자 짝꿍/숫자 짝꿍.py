def solution(X, Y):
    answer = ''
    for i in "0123456789":
        answer += i * min(X.count(i), Y.count(i))
    if not answer: return '-1'
    if answer.count('0') == len(answer): return '0'
    return ''.join(sorted(list(answer), reverse=True))