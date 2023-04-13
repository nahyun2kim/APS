import sys
input = sys.stdin.readline

# 파일의 개수
n = int(input())

# 확장자 저장
file = {}
for _ in range(n):
    extension = input().rstrip().split('.')[1]
    if extension in file.keys():
        file[extension] += 1
    else:
        file[extension] = 1

# 사전순으로 정렬해서 출력
keys = sorted(file.keys())
for i in keys:
    print(i, end=' ')
    print(file[i])