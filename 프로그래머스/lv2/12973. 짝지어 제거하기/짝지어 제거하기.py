def solution(s):
    st = []
    for s in s:
        if st and s == st[-1]:
            st.pop()
        else:
            st.append(s)
    return 0 if st else 1