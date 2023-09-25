from itertools import combinations

def solution(nums):
    l = sum(nums) + 1
    prime = []
    isprime = [0]*l
    for i in range(2, l):
        if not isprime[i]:
            prime.append(i)
            for j in range(i, l, i):
                isprime[j] = 1
    answer = 0
    for i in combinations(nums, 3):
        if sum(i) in prime:
            answer += 1
    return answer