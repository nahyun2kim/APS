import sys
input = sys.stdin.readline

n = int(input())
student = []
for _ in range(n):
    name, a, b, c = input().split()
    student.append((int(a), int(b), int(c), name))

student.sort(key = lambda x : (-x[0], x[1], -x[2], x[3]))

for x in student:
    print(x[3])