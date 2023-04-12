import sys
input = sys.stdin.readline

# 3번의 입력이 주어짐
for _ in range(3):
    # 동전의 개수
    n = int(input())
    coins = {}
    money = 0
    for _ in range(n):
        coin, cnt = map(int, input().split())
        coins[coin] = cnt
        money += coin * cnt

    if money % 2 == 1:
        print(0)
        continue

    keys = sorted(coins.keys(), key = lambda x : -x)
    c = money // 2
    dp = [1] + [0] * c
    for key in keys:
        for i in range(c, key-1, -1):
            if dp[i - key]:
                for j in range(coins[key]):
                    if i + key * j <= c:
                        dp[i + key * j] = 1
    if dp[-1]:
        print(1)
    else:
        print(0)