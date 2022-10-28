def solution(s):
    answer = 1000
    length = len(s)
    if length == 1:
        return 1
    n = length//2
    for a in range(1,n+1):
        index = list(range(0,len(s)+1,a))
        tmp = s[:index[1]]
        cnt = 1
        result = ''
        for i in range(1,len(index)-1):
            if not tmp == s[index[i]:index[i+1]]:
                if cnt == 1:
                    result += tmp
                else:
                    result += str(cnt) + tmp
                tmp = s[index[i]:index[i+1]]
                cnt = 1
            else:
                cnt += 1
        if cnt == 1:
            result += tmp
        else:
            result += str(cnt) + tmp
        result += s[index[-1]:]
        answer = min(answer, len(result))
    return answer