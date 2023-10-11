def ispalin(string):
    a, b = string[:len(string)//2], string[(-1)*(len(string)//2):]
    return a == b[::-1]

def solution(s):
    answer = 1
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if j - i > answer and ispalin(s[i:j]):
                answer = j - i
    return answer