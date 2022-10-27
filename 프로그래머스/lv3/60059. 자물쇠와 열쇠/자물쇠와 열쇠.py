def solution(key, lock):
    n = len(lock)
    m = len(key)
    check = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                check += 1
    if check == 0:
        return True
    keys = []
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                keys.append([i,j])
    for d in range(4):
        keys = rot90(keys, m)
        for ii in range(-m+1, n):
            for jj in range(-m+1, n):
                cnt = 0
                flag = True
                for i, j in keys:
                    di = i + ii
                    dj = j + jj
                    if 0<=di<n and 0<=dj<n:
                        if lock[di][dj] == 1:
                            flag = False
                            break;
                        else:
                            cnt += 1
                if flag and cnt == check:
                    return True

    return False

def rot90(arr, n):
    tmp = []
    for i,j in arr:
        tmp.append([j,n-1-i])
    return tmp
