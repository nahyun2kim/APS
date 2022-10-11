def solution(participant, completion):
    N = len(participant)
    parti = {}
    for i in range(N):
        if participant[i] in parti.keys():
            parti[participant[i]] += 1
        else:
            parti[participant[i]] = 1
    
    for name in completion:
        if parti[name] == 1:
            del(parti[name])
        else:
            parti[name] -= 1
    name = list(map(str, parti.keys()))
    answer = name[0]
    return answer