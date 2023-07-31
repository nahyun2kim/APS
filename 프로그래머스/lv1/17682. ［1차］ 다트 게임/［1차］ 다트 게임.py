def solution(dartResult):
    sdt = {'S' : 1, 'D': 2, 'T': 3}
    record = [0]
    idx = 0
    for i, d in enumerate(dartResult):
        if d in ['S', 'D', 'T']:
            record.append(int(dartResult[idx:i])**sdt[d])
        elif d == '*':
            record[-1] *= 2
            record[-2] *= 2
        elif d == '#':
            record[-1] *= -1
        else: continue
        idx = i+1
    return sum(record)