def solution(numbers):
    answer = [-1]*(len(numbers))
    st = []
    for i, n in enumerate(numbers):
        while st and numbers[st[-1]] < n:
            answer[st.pop()] = n
        st.append(i)
    return answer