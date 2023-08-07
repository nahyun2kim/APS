import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
ans = [-1]*n
st = []
for i, num in enumerate(numbers):
    while st and numbers[st[-1]] < num:
        ans[st.pop()] = num
    st.append(i)

for a in ans:
    print(a, end=' ')