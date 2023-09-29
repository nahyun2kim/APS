def solution(survey, choices):
    name = ['RT', 'CF', 'JM', 'AN']
    score = {i:0 for i in name}
    for s, c in zip(survey, choices):
        if s in score:
            score[s] += 4 - c
        else:
            score[s[::-1]] += c - 4
    answer = ''
    for n in name:
        answer += n[0] if score[n] >= 0 else n[1]
    return answer