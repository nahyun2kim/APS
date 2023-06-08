import collections
def solution(k, tangerine):
    cnt = 0
    size = collections.Counter(tangerine)
    size_list = sorted(size.values(), reverse=True)
    for i in range(len(size_list)):
        cnt += size_list[i]
        if cnt >= k:
            return i + 1