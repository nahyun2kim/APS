def solution(keymap, targets):
    key = dict()
    answer = []
    for k in keymap:
        for i, k in enumerate(k):
            if k in key.keys():
                key[k] = min(key[k], i+1)
            else:
                key[k] = i+1
    for target in targets:
        cnt = 0
        for t in target:
            if not t in key.keys():
                cnt = -1
                break
            cnt += key[t]
        answer.append(cnt)
    return answer