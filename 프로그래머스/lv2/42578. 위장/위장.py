def solution(clothes):
    cloth = {}
    for a,c in clothes:
        if c in cloth.keys():
            cloth[c] += 1
        else:
            cloth[c] = 1
    answer = 1
    for i in cloth.values():
        answer *= i+1
    return answer-1