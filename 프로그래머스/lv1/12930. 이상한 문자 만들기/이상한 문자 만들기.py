def solution(s):
    answer = ''
    idx = 0
    for s in s:
        if s == ' ':
            idx = 0
            answer += ' '
            continue
        answer += s.upper() if idx % 2 == 0 else s.lower()
        idx += 1
    return answer