def solution(s):
    l = len(s) // 2
    return s[l] if len(s)%2 == 1 else s[l-1:l+1]