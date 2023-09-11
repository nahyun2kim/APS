def solution(s):
    answer = []
    idx = {}
    for i, s in enumerate(s):
        answer.append(i-idx[s] if s in idx.keys() else -1)
        idx[s] = i
    return answer