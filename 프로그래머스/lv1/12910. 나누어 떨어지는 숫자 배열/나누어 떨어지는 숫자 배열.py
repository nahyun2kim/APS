def solution(arr, divisor):
    answer = [i for i in sorted(arr) if i % divisor == 0]
    return answer if answer else [-1]