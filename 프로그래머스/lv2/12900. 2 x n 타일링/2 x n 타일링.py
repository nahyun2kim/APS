def solution(n):
    tiles = [-1]*(n+1)
    tiles[0] = 1
    tiles[1] = 1
    for i in range(2, n+1):
        tiles[i] = (tiles[i-1]+tiles[i-2])%1000000007
    return tiles[n]