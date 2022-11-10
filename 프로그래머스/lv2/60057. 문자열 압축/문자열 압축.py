def solution(s):
    # 미리 세팅해둔 최솟값
    answer = len(s)
    # 문자열의 길이가 이미 1이라면 바로 return 1
    if len(s) == 1: return 1
    # 단위를 전체 길이의 반까지만 보면 됨
    n = len(s)//2

    for a in range(1,n+1):
        flag = s[:a]
        l = a
        cnt = 1
        for i in range(a, len(s), a):
            if i + a > len(s):
                break
            if s[i:i+a] == flag:
                cnt += 1
            else:
                if not cnt == 1:
                    l += len(str(cnt))
                flag = s[i:i+a]
                cnt = 1
                l += a
        if not cnt == 1:
            l += len(str(cnt))
        answer = min(answer, l+len(s)%a)

    return answer