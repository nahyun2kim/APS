def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        st = list(reversed(skill))
        flag = True
        for a in s:
            if not a in st:
                continue
            elif a == st[-1]:
                st.pop()
            else:
                flag = False
                break
        if flag: answer += 1
    return answer