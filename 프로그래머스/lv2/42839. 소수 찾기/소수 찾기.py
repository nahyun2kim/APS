from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    prime = []
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            j = ''.join(j)
            j = int(j)
            if not j in prime and not j == 1 and not j == 0:
                if j == 2:
                    prime.append(j)
                    continue
                flag = True
                for k in range(2, int(j**0.5)+1):
                    if j % k == 0:
                        flag = False
                        break
                if flag:
                    prime.append(j)
    return len(prime)