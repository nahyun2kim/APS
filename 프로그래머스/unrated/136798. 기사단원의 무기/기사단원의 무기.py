def solution(number, limit, power):
    def cal(n):
        cnt = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                cnt += 1
        if int(n**0.5)**2 == n:
            return cnt*2 - 1
        return cnt*2
    answer = 0
    for i in range(1, number + 1):
        answer += cal(i) if cal(i) <= limit else power
    return answer