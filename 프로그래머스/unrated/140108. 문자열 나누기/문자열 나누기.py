def solution(s):
    answer = 0
    x = ''
    cnt1 = cnt2 = 0
    for s in s:
        if not x:
            x = s
            cnt1 += 1
            continue
        if s == x:
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            answer += 1
            x = ''
            cnt1 = cnt2 = 0
    return answer if not x else answer + 1