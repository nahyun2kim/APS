def solution(s):
    num2str = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 
               'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    answer = ''
    idx = 0
    for i in range(len(s)):
        if s[i].isdigit(): 
            answer += s[i]
            idx = i+1
        else:
            if s[idx:i+1] in num2str.keys():
                answer += num2str[s[idx:i+1]]
                idx = i+1
    return int(answer)