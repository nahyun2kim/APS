def solution(data, ext, val_ext, sort_by):
    answer = []
    cols = ['code', 'date', 'maximum', 'remain']
    for i in range(len(data)):
        if data[i][cols.index(ext)] < val_ext:
            answer.append(data[i])
    return sorted(answer, key = lambda x:x[cols.index(sort_by)])