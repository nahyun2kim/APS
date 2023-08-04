def solution(msg):
    answer = []
    dic = {a:i+1 for i, a in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))}
    i = 0
    while i < len(msg):
        j = i + 1
        while j <= len(msg):
            if msg[i:j] in dic.keys():
                j += 1
            else:
                dic[msg[i:j]] = len(dic) + 1
                break
        answer.append(dic[msg[i:j-1]])
        i = j - 1
    return answer