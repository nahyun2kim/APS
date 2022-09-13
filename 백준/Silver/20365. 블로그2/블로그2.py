#1. 입력받기
N = int(input())
test = input()

#2. 시작색 체크 & 갯수 세기
cnt = 1
if test[0] == 'B':
    for i in range(len(test)-1):
        if test[i] == 'B' and test[i+1] == 'R':
            cnt += 1
            
else:
    for i in range(len(test)-1):
        if test[i] == 'R' and test[i+1] == 'B':
            cnt += 1

#3. 갯수 출력            
print(cnt)