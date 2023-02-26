# boj S4 1065
# 브루트포스

n = int(input())

nums = [111, 123, 135, 147, 159, 210, 222, 234, 246, 258,
321, 333, 345, 357, 369, 420, 432, 444, 456, 468,
531, 543, 555, 567, 579, 630, 642, 654, 666, 678,
741, 753, 765, 777, 789, 840, 852, 864, 876, 888,
951, 963, 975, 987, 999]

ans = 0

if n < 100:
    ans = n
elif n <= 110:
    ans = 99
elif n == 1000:
    ans = 99 + len(nums)
else:
    for i in range(len(nums)):
        if nums[i] == n:
            ans = 100 + i
            break
        elif nums[i] > n:
            ans = 99 + i
            break

print(ans)