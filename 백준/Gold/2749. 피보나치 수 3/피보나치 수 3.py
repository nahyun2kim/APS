import sys
input = sys.stdin.readline

# n번째 피보나치 수
n = int(input())
m = 1000000         # 10^6
p = 15 * (m // 10)  # 피사노주기에 의해 15 * 10^(6-1)
n %= p

a, b = 0, 1
for i in range(n):
  a, b = b % m, (a + b) % m

print(a)