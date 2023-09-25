def solution(food):
    answer = '0'
    for i in range(len(food)-1, 0, -1):
        f = str(i)*(food[i]//2)
        answer = f + answer + f
    return answer