def solution(cards1, cards2, goal):
    for g in goal:
        if cards1 and g == cards1[0]:
            cards1.pop(0)
        elif cards2 and g == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'