def solution(s, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for sk in skip:
        alpha = alpha.replace(sk, '')
    answer = ''
    for s in s:
        answer += alpha[(alpha.index(s)+index)%len(alpha)]
    return answer