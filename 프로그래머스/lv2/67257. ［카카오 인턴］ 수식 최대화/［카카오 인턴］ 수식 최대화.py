from itertools import permutations

def cal(idx, array, num):
    sign = array[idx]
    tmp = []
    for i in num.split(sign):
        tmp.append(i if i.isdigit() else cal(idx+1, array, i))
    return str(eval(sign.join(tmp)))

def solution(expression):
    answer = 0
    기호 = ['*', '-', '+']
    for i in permutations(기호, 3):
        n = cal(0, i, expression)
        answer = max(answer, abs(int(n)))
    return answer