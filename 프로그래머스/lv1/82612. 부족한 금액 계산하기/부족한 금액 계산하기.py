def solution(price, money, count):
    answer = price * sum(range(1, count+1)) - money
    return answer if answer > 0 else 0