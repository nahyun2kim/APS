def solution(n, computers):
    answer = 0
    visit = [0]*n
    def dfs(x):
        st = [x]
        while st:
            now = st.pop()
            for i, c in enumerate(computers[now]):
                if not visit[i] and c == 1:
                    visit[i] = 1
                    st.append(i)
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            dfs(i)
            answer += 1
    return answer