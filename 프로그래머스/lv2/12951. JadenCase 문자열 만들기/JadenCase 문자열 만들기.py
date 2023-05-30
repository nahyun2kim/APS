def solution(s):
    arr = s.split(" ")
    answer = []
    for arr in arr:
        if arr == '':
            answer.append(arr)
        elif arr[0].isalpha():
            answer.append(arr[0].upper() + arr[1:].lower())
        else:
            answer.append(arr[0] + arr[1:].lower())
    return " ".join(answer)