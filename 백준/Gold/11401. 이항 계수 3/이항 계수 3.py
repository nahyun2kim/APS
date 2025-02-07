import sys
N, K = map(int, sys.stdin.readline().split(' '))
p = 1000000007

# 팩토리얼 (나머지 정리 적용)
def factorial(n):
  answer = 1
  for i in range(2, n + 1):
    answer = answer * i % p
  return answer

# 거듭제곱 (나머지 정리 적용)
def power(n, k):
  if k == 0:
    return 1
  if k == 1:
    return n
  
  tmp = power(n, k//2)
  if k % 2:
    return tmp * tmp * n % p
  else:
    return tmp * tmp % p
  
a = factorial(N)
b = factorial(N - K) * factorial(K) % p

print(a * power(b, p-2) % p)