def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col-1], -x[0]))
    for i in range(row_begin - 1, row_end):
        s = 0
        for d in data[i]:
            s += d % (i + 1)
        answer ^= s
    return answer