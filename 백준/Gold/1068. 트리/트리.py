N = int(input())
input_list = list(map(int,input().split()))
arr =[[] for _ in range(N)]
for i in range(N):
    super = input_list[i]
    if super != -1:
        arr[super].append(i)
    else:
        arr[i].append(-1)
        
def delete(arr, node):
    if len(arr[node]) == 0:
        arr[node].append(-2)
        return
    for i in arr[node][::-1]:
        arr[node].remove(i)
        delete(arr, i)
    arr[node].append(-2)

delete_node = int(input())

if -1 in arr[delete_node]:
    arr[delete_node].remove(-1)
    delete(arr, delete_node)
else:
    delete(arr, delete_node)
    arr[input_list[delete_node]].remove(delete_node)

cnt = 0
for node in arr:
    if len(node)==0:
        cnt += 1
    elif len(node)==1 and -1 in node:
        cnt += 1

print(cnt)