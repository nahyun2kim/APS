def solution(numbers, hand):
    answer = ''
    l = [1, 3]
    r = [3, 3]
    for n in numbers:
        if n % 3 == 1:
            answer += 'L'
            l[0] = 1
            l[1] = n // 3
        elif n and n % 3 == 0:
            answer += 'R'
            r[0] = 3
            r[1] = n // 3 - 1
        else:
            if n == 0: n = 11
            ld = abs(l[0] - 2) + abs(l[1] - n // 3)
            rd = abs(r[0] - 2) + abs(r[1] - n // 3)
            if ld < rd:
                answer += 'L'
                l[0] = 2
                l[1] = n // 3
            elif rd < ld:
                answer += 'R'
                r[0] = 2
                r[1] = n // 3
            else:
                if hand == 'right':
                    answer += 'R'
                    r[0] = 2
                    r[1] = n // 3
                else:
                    answer += 'L'
                    l[0] = 2
                    l[1] = n // 3
    return answer