def solution(number, k):
    answer = ''
    idx = 0
    delete = 0
    while idx < len(number) and delete < k and len(answer) < len(number)-k:
        index, max_value = -1, -1
        for i in range(idx, idx+k-delete+1):
            if int(number[i]) == 9:
                index = i
                break
            if i < len(number) and int(number[i]) > max_value:
                max_value = int(number[i])
                index = i
        for i in range(idx, index):
            delete += 1
        answer += number[index]
        idx = index+1
        
    if not idx == len(number) and len(answer) < len(number)-k:
        answer += number[idx:]
    
    return answer