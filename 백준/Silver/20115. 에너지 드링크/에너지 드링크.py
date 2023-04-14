import sys
input = sys.stdin.readline

# 에너지 드링크의 수
n = int(input())

# 드링크를 최대한 적게 버리기 위해 적은 양으로 정렬
drink = list(map(int, input().split()))
drink.sort()

answer = drink[-1]
answer += sum(drink[:n-1]) / 2

print(answer)