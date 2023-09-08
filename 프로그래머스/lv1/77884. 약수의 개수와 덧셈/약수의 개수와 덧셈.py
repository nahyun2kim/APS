def divisor(n):
    l = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            l.append(i)
            if not n // i == i: l.append(n // i)
    return len(l)

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        d = divisor(i)
        answer += i if d % 2 == 0 else -i
    return answer