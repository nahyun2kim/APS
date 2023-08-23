from math import gcd

def solution(arrayA, arrayB):
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    for a, b in zip(arrayA, arrayB):
        gcdA = gcd(gcdA, a)
        gcdB = gcd(gcdB, b)
    answer = 0
    for i in range(gcdA, 0, -1):
        if gcdA % i == 0:
            flag = True
            for b in arrayB:
                if b % i == 0:
                    flag = False
                    break
            if flag:
                answer = max(answer, i)
                break
    for i in range(gcdB, answer, -1):
        if gcdB % i == 0:
            flag = True
            for a in arrayA:
                if a % i == 0:
                    flag = False
                    break
            if flag:
                answer = max(answer, i)
                break
    return answer