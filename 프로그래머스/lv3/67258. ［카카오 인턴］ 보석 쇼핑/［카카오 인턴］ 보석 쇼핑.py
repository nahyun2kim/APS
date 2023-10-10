def solution(gems):
    n = len(set(gems))
    종류 = {gems[0] : 1}
    st = 0
    ed = 1
    answer = [0, len(gems)]
    while st < ed and ed <= len(gems):
        if len(종류) == n:
            if ed - st < answer[1] - answer[0]:
                answer = [st, ed]
            종류[gems[st]] -= 1
            if 종류[gems[st]] == 0: 종류.pop(gems[st])
            st += 1
        else:
            if ed < len(gems):
                if gems[ed] in 종류:
                    종류[gems[ed]] += 1
                else:
                    종류[gems[ed]] = 1
            ed += 1
    return [answer[0]+1, answer[1]]