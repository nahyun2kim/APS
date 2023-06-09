def solution(s):
    answer = []
    s = list(s[2:-2].split('},{'))
    s.sort(key = lambda x : len(x))
    for s in s:
        for s in s.split(','):
            if not int(s) in answer:
                answer.append(int(s))
                break
    return answer