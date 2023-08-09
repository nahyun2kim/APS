def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            tmp = bin(number)[2:]
            cnt = 0
            for t in reversed(tmp):
                if t == '1':
                    cnt += 1
                else:
                    break
            answer.append(number + 2 ** (cnt - 1))
    return answer