import sys
input = sys.stdin.readline

# 에너지 드링크의 수
n = int(input())

# 드링크를 최대한 적게 버리기 위해 적은 양으로 정렬
drink = list(map(int, input().split()))
drink.sort()

answer = drink[-1]
for i in range(n-1):
    answer += drink[i] / 2

if answer * 10 % 10 == 0:
    print(int(answer))
else:
    print(round(answer, 5))