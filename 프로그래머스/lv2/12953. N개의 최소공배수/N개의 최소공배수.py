def lcm(a, b):
    for i in range(max(a, b), a*b+1):
        if i%a == 0 and i%b == 0:
            return i

def solution(arr):
    answer = 0
    st = arr[:]
    while len(st) > 1:
        a = st.pop()
        b = st.pop()
        st.append(lcm(a, b))
    return st[0]