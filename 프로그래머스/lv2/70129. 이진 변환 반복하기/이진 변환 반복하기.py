def solution(s):
    zero = 0
    change = 0
    while s != '1':
        zero += s.count('0')
        s = '1'*s.count('1')
        s = bin(len(s))[2:]
        change += 1
    answer = [change, zero]
    return answer