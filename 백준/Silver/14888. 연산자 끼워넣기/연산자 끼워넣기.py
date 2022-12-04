import sys
input = sys.stdin.readline

# n: 수의 개수
n = int(input())

# 숫자의 정보
num = list(map(int, input().split()))

# 연산자 정보
operator = list(map(int, input().split()))

def num_to_oper(i, x, y):
    global res
    if i == 0:
        return x + y
    elif i == 1:
        return x - y
    elif i == 2:
        return x * y
    else:
        if x >= 0:
            return x // y
        else:
            return -((-x)//y)

def dfs(idx, ans):
    global max_ans, min_ans
    if idx == n:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return
    
    for o in range(4):
        if operator[o] == 0:
            continue
        operator[o] -= 1
        dfs(idx+1, num_to_oper(o, ans, num[idx]))
        operator[o] += 1

max_ans = -sys.maxsize
min_ans = sys.maxsize

dfs(1, num[0])
print(max_ans)
print(min_ans)