def solution(sequence, k):
    end = len(sequence) - 1
    answer = [0, end]
    min_cnt = len(sequence)
    for i, s in enumerate(sequence):
        if s == k:
            return [i, i]
        if s > k:
            end = i
            break
            
    seq = 0
    ed = end
    for i in range(end, -1, -1):
        st = i
        seq += sequence[i]
        if seq == k and answer[1] - answer[0] >= ed - st:            
            answer = [st, ed]
        elif seq > k:
            seq -= sequence[ed]
            ed -= 1
            if seq == k:
                answer = [st, ed]
    return answer