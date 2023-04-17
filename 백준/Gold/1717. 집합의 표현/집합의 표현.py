import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if rep[x] == x:
        return x
    rep[x] = find(rep[x])
    return rep[x]

# n: 초기 집합, m: 연산 개수
n, m = map(int ,input().split())

rep = {i:i for i in range(n+1)}

# 연산 입력
for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        ra = find(a)
        rb = find(b)
        if ra <= rb:
            rep[rb] = ra
        else:
            rep[ra] = rb
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
