s = input()
cnt = 0
for i in range(1,len(s)):
    if not s[i-1] == s[i]:
        cnt += 1
print((cnt+1)//2)