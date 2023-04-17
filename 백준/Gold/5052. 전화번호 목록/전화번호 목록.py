import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    phone = []
    for _ in range(n):
        phone.append(input().rstrip())
    phone.sort(key=lambda x : len(x))
    check = {}
    flag = False
    for p in phone:
        for i in range(1, len(p)):
            check[p[:i]] = 1
    for p in phone:
        if p in check.keys():
            flag = True
            break
    if flag:
        print('NO')
    else:
        print('YES')