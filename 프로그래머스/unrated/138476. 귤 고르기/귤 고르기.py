def solution(k, tangerine):
    cnt = 0
    size = {}
    for t in tangerine:
        if t in size.keys():
            size[t] += 1
        else:
            size[t] = 1
    size_list = []
    for v in size.values():
        size_list.append(v)
        
    size_list.sort(reverse=True)
    for i in range(len(size_list)):
        cnt += size_list[i]
        if cnt >= k:
            return i + 1