def canAddLength(park, r, c, n):
    row, col = len(park), len(park[0])
    for i in range(n + 1):
        if r + i >= row or c + n >= col or park[r + i][c + n] != "-1":
            return False
    for i in range(n):
        if r + n >= row or c + i >= col or park[r + n][c + i] != "-1":
            return False
    return True

def solution(mats, park):
    mats.sort(reverse=True)
    row, col = len(park), len(park[0])
    maxLength = 1
    for i in range(row):
        for j in range(col):
            if park[i][j] == "-1":
                length = 1
                while length < min(row, col):
                    if not canAddLength(park, i, j, length):
                        break
                    length += 1
                maxLength = max(maxLength, length)
                if maxLength >= mats[0]:
                    return mats[0]
    for mat in mats:
        if mat <= maxLength:
            return mat
    
    return -1