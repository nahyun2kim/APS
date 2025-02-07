import sys
input = sys.stdin.readline
N, B = map(int, input().split(' '))
p = 1000

# 행렬 A
A = []
for _ in range(N):
  a = list(map(int, input().split(' ')))
  A.append(a)

# 행렬 곱셈 (n * n 행렬) (나머지 연산 포함)
def cross(X, Y):
  n = len(X)
  new = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      value = 0
      for k in range(n):
        value += X[i][k] * Y[k][j] % p
      new[i][j] = value % p
  return new

def dac(matrix, num):
  if num == 1:
    for i in range(N):
      for j in range(N):
        matrix[i][j] %= p
    return matrix
  mat = dac(matrix, num // 2)
  if num % 2:
    return cross(cross(mat, mat), matrix)
  else:
    return cross(mat, mat)

answer = dac(A, B)

for answer in answer:
  print(*answer)