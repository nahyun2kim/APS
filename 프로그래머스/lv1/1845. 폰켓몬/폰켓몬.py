def solution(nums):
    answer = 0
    numbers = set(nums)
    if len(numbers) < len(nums) // 2:
        answer = len(numbers)
    else:
        answer = len(nums) // 2
    return answer