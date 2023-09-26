def solution(babbling):
    standard = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for b in babbling:
        flag = True
        for a in standard:
            if a*2 in b:
                flag = False
                break
            if a in b:
                b = b.replace(a, ' ')
        if not flag:
            continue
        if b.rstrip() == '':
            answer += 1
    return answer