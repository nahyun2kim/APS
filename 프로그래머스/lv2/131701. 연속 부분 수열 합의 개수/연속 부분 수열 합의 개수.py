def solution(elements):
    answer = elements[:] + [sum(elements)]
    for j in range(len(elements)):
        tmp = elements[j]
        for k in range(1, len(elements)):
            tmp += elements[j+k] if 0 <= j+k < len(elements) else elements[j+k-len(elements)]
            answer.append(tmp)
    return len(set(answer))