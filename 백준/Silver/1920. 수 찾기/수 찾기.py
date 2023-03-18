# boj 1920 S4 수 찾기
# 자료구조 # 정렬 # 이분탐색

import sys
input = sys.stdin.readline

# n개의 정수
n = int(input())
nums = list(map(int, input().split()))

# m개의 판단할 수
m = int(input())
check = list(map(int, input().split()))

# nums 정렬
nums.sort()

# 이분탐색 실행
def binary_search(st ,ed, find):
    flag = False
    while st <= ed:
        mid = (st + ed) // 2
        if nums[mid] == find:
            flag = True
            print(1)
            break
        elif nums[mid] > find:
            ed = mid - 1
        else:
            st = mid + 1

    if not flag:
        print(0)

for c in check:
    binary_search(0, n-1, c)
