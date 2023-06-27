def solution(record):
    order = []
    name = {}
    for rcd in record:
        info = list(rcd.split())
        if info[0] == 'Enter':
            order.append((1, info[1]))
            name[info[1]] = info[2]
        elif info[0] == 'Leave':
            order.append((0, info[1]))
        else:
            name[info[1]] = info[2]
    answer = []
    for io, ID in order:
        answer.append(name[ID]+'님이 들어왔습니다.' if io else name[ID]+'님이 나갔습니다.')
    return answer