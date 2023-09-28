def solution(s, n):
    l = 'abcdefghijklmnopqrstuvwxyz'
    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for s in s:
        if s == ' ':
            answer += ' '
        elif s.islower():
            idx = l.index(s) + n
            answer += l[idx if idx < 26 else idx-26]
        else:
            idx = u.index(s) + n
            answer += u[idx if idx < 26 else idx-26]
    return answer