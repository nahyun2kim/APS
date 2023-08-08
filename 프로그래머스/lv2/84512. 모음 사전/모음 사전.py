def solution(word):
    words = ['U', 'O', 'I', 'E', 'A']
    answer = 0
    st = words[:]
    while st:
        now = st.pop()
        answer += 1
        if now == word:
            return answer
        if len(now) == 5: continue
        for w in words:
            st.append(now + w)