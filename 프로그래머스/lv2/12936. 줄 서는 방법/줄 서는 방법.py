import math
def solution(n, k):
    answer = []
    nums = [i for i in range(1, n+1)]    
    for idx in range(n, 1, -1):
        x = math.factorial(idx - 1)
        for i, n in enumerate(nums):
            if i*x < k <= (i+1)*x:
                answer.append(n)
                nums.remove(n)
                k -= i*x
                break
    return answer + nums