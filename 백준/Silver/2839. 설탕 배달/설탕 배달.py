import sys
input = sys.stdin.readline

N = int(input())

five = N//5
while five >= 0:
    if (N - 5*five)%3 != 0:
        five -= 1
        continue
    three = (N - 5*five)//3
    break
    
if five < 0:
    ans = -1
else:
    ans = five + three
    
print(ans)