def solution(topping):
    answer = 0
    a = set()
    b = {}
    for i in topping:
        b[str(i)] = b.get(str(i), 0)
        b[str(i)] += 1
    for i in topping:
        a.add(i)
        b[str(i)] -= 1
        if b[str(i)] == 0:
            del b[str(i)]
        if len(a) == len(b.keys()):
            answer += 1
    return answer