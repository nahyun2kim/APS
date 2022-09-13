#1. 입력 
K = int(input()) # K : 레벨
buil = list(map(int, input().split())) # 들어간 순서대로 빌딩의 번호

#2. 레벨을 숫자로 풀어써주는
num = []
def level_to_num(idx):
    if idx<=K:
        level_to_num(idx+1)
        num.append(idx)
        level_to_num(idx+1)

level_to_num(1)

#3. 레벨의 리스트를 만들고 숫자에 맞게 넣어주자
level = [[] for _ in range(K+1)] # 레벨은 1부터 K까지이므로 하나더 추가해서 만듦
for i in range(len(num)):
    idx = num[i]
    level[idx].append(buil[i])

#4. 레벨 별로 출력
for i in range(1, K+1):
    lev = list(map(str, level[i]))
    print(" ".join(lev))