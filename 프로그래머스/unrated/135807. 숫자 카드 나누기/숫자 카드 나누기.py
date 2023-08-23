from math import gcd

def solve(gcdN, minValue, array):
    for i in range(gcdN, minValue, -1):
        if gcdN % i == 0:
            flag = True
            for a in array:
                if a % i == 0:
                    flag = False
                    break
            if flag:
                return i
    return 0

def solution(arrayA, arrayB):
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    for a, b in zip(arrayA, arrayB):
        gcdA = gcd(gcdA, a)
        gcdB = gcd(gcdB, b)
    answer = 0
    answer = max(answer, solve(gcdA, answer, arrayB))
    answer = max(answer, solve(gcdB, answer, arrayA))
    return answer