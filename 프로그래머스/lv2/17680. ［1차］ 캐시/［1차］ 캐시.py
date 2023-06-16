from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque(maxlen = cacheSize)
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            answer += 5
            q.append(city)
    return answer