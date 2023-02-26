# boj S2 1411 비슷한 단어
# 문자열 # 브루트포스

n = int(input())
words = []
for _ in range(n):
    words.append(input())

ans = 0
for i in range(n):
    for j in range(i+1, n):
        length = len(words[i])
        check = {}
        flag = True
        for l in range(length):
            if words[i][l] in check.keys():
                if check[words[i][l]] != words[j][l]:
                    flag = False
                    break
            else:
                if words[j][l] in check.values():
                    flag = False
                    break
                check[words[i][l]] = words[j][l]
        if flag:
            ans += 1
        # print(i, j, ans)

print(ans)