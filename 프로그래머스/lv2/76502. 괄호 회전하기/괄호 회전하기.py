def solution(s):
    answer = 0
    bracket = {')':'(', '}':'{', ']':'['}
    def isRight(string):
        st = []
        for s in string:
            if s in ['(', '{', '[']:
                st.append(s)
            elif st and bracket[s] == st[-1]:
                st.pop()
            else:
                return False
        return len(st) == 0
    for i in range(len(s)):
        string = s[i:] + s[:i]
        if isRight(string):
            answer += 1
    return answer