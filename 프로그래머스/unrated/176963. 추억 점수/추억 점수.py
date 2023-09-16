def solution(name, yearning, photo):
    score = {i: j for i, j in zip(name, yearning)}
    return [sum([score[i] if i in score.keys() else 0 for i in p]) for p in photo]
