# boj 1527 S1 금민수의 개수
# 브루트포스

a, b = map(int, input().split())
ans = 0

nums = ['4', '7']
st = len(str(a))
ed = len(str(b))

def make_num(cnt, sel, k):
    global ans
    if cnt == k:
        if a <= int(sel) <= b:
            ans += 1
        return

    make_num(cnt + 1, sel + '4', k)
    make_num(cnt + 1, sel + '7', k)

for i in range(st, ed + 1):
    make_num(0, '', i)

print(ans)