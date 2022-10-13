def solution(n, t, m, p):
    
    #10진수 -> n진수
    def change(num, q):
        tmp = ''
        while num > 0:
            num, mod = divmod(num, q)
            if mod >= 10:
                tmp += chr(55+mod)
            else:
                tmp += str(mod)
        return tmp[::-1]
    
    idx, num, th = 0, 0, 0
    str_num = '0'
    answer = ''
    while(len(answer) < t):
        if idx%m == p-1:
            answer += str_num[th]
        th += 1
        if th == len(str_num):
            num += 1
            str_num = change(num, n)
            th = 0
        idx += 1
        
    return answer