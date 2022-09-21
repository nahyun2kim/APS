import sys
input = sys.stdin.readline

def position(idx, ability):
    global ans, check, player
    
    if idx == 11:
        ans = max(ans, ability)
        return
    
    for i in range(11):
        if check[i] == True or player[i][idx] == 0:
            continue
        check[i] = True
        position(idx+1, ability+player[i][idx])
        check[i] = False

T = int(input())
for _ in range(T):
    player = []
    for _ in range(11):
        player.append(list(map(int,input().split())))
    
    ans = 0
    check = [False]*11
    position(0, 0)
    
    print(ans)
    