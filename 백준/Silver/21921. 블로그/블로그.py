import sys
input = sys.stdin.readline

# n: 블로그를 시작하고 지난 일수, x: 탐색할 기간
n, x = map(int, input().split())

# 방문자 수
visit = list(map(int, input().split()))

# 누적합 구하기
visit_sum = [0, visit[0]]
for i in range(1, n):
    visit_sum.append(visit_sum[i] + visit[i])

# 돌면서 최대값 구하기
ans = []
for i in range(x, n+1):
    ans.append(visit_sum[i] - visit_sum[i-x])

ans.sort( key = lambda x : -x )

if ans[0] == 0:
    print('SAD')
else:
    day = 0
    answer = ans[0]
    for a in ans:
        if answer == a:
            day += 1
        else:
            break
    print(answer)
    print(day)