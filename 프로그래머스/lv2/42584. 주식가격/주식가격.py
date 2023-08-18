def solution(prices):
    answer = [0] * len(prices)
    st = []
    for i, price in enumerate(prices):
        while st and st[-1][1] > price:
            idx, p = st.pop()
            answer[idx] = i - idx
        st.append((i, price))
    while st:
        idx, p = st.pop()
        answer[idx] = len(prices) - idx - 1
    return answer