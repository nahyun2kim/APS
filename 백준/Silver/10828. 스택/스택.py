import sys

N = int(input())
stack = []

for _ in range(N):
    com = sys.stdin.readline().strip()
    if "push" in com:
        num = com.split()[1]
        stack.append(int(num))
    elif "pop" == com:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif "size" == com:
        print(len(stack))
    elif "empty" == com:
        if not stack:
            print(1)
        else:
            print(0)
    elif "top" == com:
        if not stack:
            print(-1)
        else:
            print(stack[-1])