import sys
input = sys.stdin.readline

N, M = map(int, input().split())
coord = list(map(int,input().split()))
coord.sort()

def find_point(target, flag):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end)//2
        if coord[mid] < target:
            start = mid+1
        elif coord[mid] > target:
            end = mid-1
        else:
            return mid
    if flag == 0:
        return start
    else:
        return end

for _ in range(M):
    s, e = map(int, input().split())
    print(find_point(e, 1)-find_point(s, 0)+1)