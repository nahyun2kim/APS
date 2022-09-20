import sys
input = sys.stdin.readline

N = int(input())

start = 0
end = N
while start <= end:
    mid = (start + end) // 2
    if mid**2 < N:
        start = mid + 1
    elif mid**2 > N: 
        end = mid - 1
    else:
        start = mid
        break

print(start)