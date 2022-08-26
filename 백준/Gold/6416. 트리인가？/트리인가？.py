from collections import deque 
import sys
input = sys.stdin.readline

def findroot(key, pl):
    dq = deque([key])
    check = []

    while dq:
        now = dq.popleft()
        if now in check:
            return False
        else:
            check.append(now)
            
        if not now in pl:
            return False
        else:
            if parents[now][0] == root:
                continue
            else:
                dq.append(parents[now][0])
    return True

fr = 1
to = 1
idx = 0
while True :
    idx += 1
    parents = {}
    subs = {}
    enter = 0
    while True :
        node_list = list(map(int, input().split()))
        if len(node_list) == 0:
            idx -= 1
            enter = 1
            break
        
        for i in range(int(len(node_list)/2)):
            fr = node_list[2*i]
            to = node_list[2*i+1]
            if fr>0 and to>0:
                if to in parents:
                    parents[to].append(fr)
                else:
                    parents[to] = [fr]
                if fr in subs:
                    subs[fr].append(to)
                else:
                    subs[fr] = [to]

        if fr <= 0 and to <= 0 :
            break
    if enter == 1:
        continue

    ans = "a tree."
            
    for value in parents.values():
        if(len(value))>1:
            ans = "not a tree."

    root = 0
    cnt = 0
    for key in subs.keys():
        if not key in parents.keys():
            root = key
            cnt += 1
    if not cnt == 1:
        ans = "not a tree."
    else:
        parents_list = list(parents.keys())
        
        for key in parents.keys():
            res = findroot(key, parents_list) 
            if res == False:
                ans = "not a tree."
                break

    if len(parents) == 0:
        ans = "a tree."
       
    if fr < 0 and to < 0 and len(node_list) == 2:
        break
    elif fr < 0 and to < 0:
        print("Case {} is {}".format(idx, ans))
        break
    else:
        print("Case {} is {}".format(idx, ans))