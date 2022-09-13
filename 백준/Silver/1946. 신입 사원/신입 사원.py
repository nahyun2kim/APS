T = int(input())
for _ in range(T):
    N = int(input())
    grade = []
    res = []
    for _ in range(N):
        doc, inv = map(int,input().split())
        grade.append((doc, inv))
    
    doc = sorted(grade, key = lambda x : x[0])
    inv = sorted(grade, key = lambda x : x[1])
    idx = 0
    while doc:
        tmp = inv[idx][0]
        if tmp < len(doc):
            del doc[tmp:]
            res.append(doc.pop())
        elif tmp == len(doc):
            res.append(doc.pop())
        idx += 1
    print(len(res))