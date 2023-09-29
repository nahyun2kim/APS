def solution(ingredient):
    ingredient = ''.join(map(str, ingredient))
    answer = 0
    st = []
    for i in ingredient:
        st.append(i)
        if len(st) > 3 and ''.join(st[-4:]) == '1231':
            st.pop()
            st.pop()
            st.pop()
            st.pop()
            answer += 1
    return answer