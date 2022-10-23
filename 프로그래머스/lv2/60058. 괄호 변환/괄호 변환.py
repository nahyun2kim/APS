def solution(p):
    if p == '':
        return ''
    answer = sol(p)
    return answer

def div(s):
    left = 0
    right = 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left > 0 and left == right:
            return i

def check(s):
    stack = []
    if s[0] == ')':
        return False
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False
    
def sol(s):
    if s == '':
        return ''
    idx = div(s)
    u = s[:idx+1]
    v = s[idx+1:]
    if check(u):
        return u+sol(v)
    else:
        tmp = ''
        for i in range(1,len(u)-1):
            if u[i] == '(':
                tmp += ')'
            else:
                tmp += '('
        return '('+sol(v)+')'+tmp