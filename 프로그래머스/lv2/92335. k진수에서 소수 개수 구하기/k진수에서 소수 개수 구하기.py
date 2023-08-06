def solution(n, k):
    
    answer = 0
    new = ''
    while n > 0:
        n, mod = divmod(n, k)
        new = str(mod) + new
    for num in list(new.split('0')):
        if num and not num == '1':
            flag = True
            for i in range(2, int(int(num)**0.5)+1):
                if int(num) % i == 0:
                    flag = False
                    break
            if flag:
                answer += 1
    return answer